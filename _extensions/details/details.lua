-- Lua filter for creating collapsible details sections in Quarto
-- Supports HTML, PDF (LaTeX), and EPUB outputs

local function ensure_html_class(el, class)
  if el.classes then
    if not el.classes:includes(class) then
      table.insert(el.classes, class)
    end
  else
    el.classes = {class}
  end
  return el
end

-- Process Div blocks with class "details"
function Div(el)
  if el.classes:includes("details") then
    local summary_text = "Show Answer"
    local content_blocks = {}
    
    -- Extract summary if provided as first header
    if #el.content > 0 and el.content[1].t == "Header" then
      summary_text = pandoc.utils.stringify(el.content[1])
      -- Remove the header from content
      for i = 2, #el.content do
        table.insert(content_blocks, el.content[i])
      end
    else
      content_blocks = el.content
    end
    
    if FORMAT:match("html") then
      -- HTML output: Use native details/summary
      local details_html = string.format([[
<details class="exercise-solution">
  <summary>%s</summary>
  <div class="details-content">
]], summary_text)
      
      return {
        pandoc.RawBlock('html', details_html),
        pandoc.Div(content_blocks, {class = "details-inner"}),
        pandoc.RawBlock('html', '</div></details>')
      }
      
    elseif FORMAT:match("latex") then
      -- LaTeX output: Use tcolorbox
      local latex_start = string.format([[\begin{detailsbox}[%s]]], summary_text)
      local latex_end = [[\end{detailsbox}]]
      
      return {
        pandoc.RawBlock('latex', latex_start),
        pandoc.Div(content_blocks),
        pandoc.RawBlock('latex', latex_end)
      }
      
    elseif FORMAT:match("epub") then
      -- EPUB output: Use styled div with disclosure triangle
      local epub_html = string.format([[
<div class="details-container">
  <div class="details-summary" onclick="this.parentElement.classList.toggle('open')">
    <span class="details-arrow">▶</span> %s
  </div>
  <div class="details-content">
]], summary_text)
      
      return {
        pandoc.RawBlock('html', epub_html),
        pandoc.Div(content_blocks),
        pandoc.RawBlock('html', '</div></div>')
      }
      
    else
      -- Fallback: Simple formatted block
      local header = pandoc.Header(4, summary_text)
      local rule = pandoc.HorizontalRule()
      table.insert(content_blocks, 1, rule)
      table.insert(content_blocks, 1, header)
      
      return pandoc.Div(content_blocks, {class = "details-fallback"})
    end
  end
end

-- Process inline Code with class "details-inline"
function Code(el)
  if el.classes:includes("details-inline") then
    local text = el.text
    
    if FORMAT:match("html") then
      return pandoc.RawInline('html', string.format(
        '<details class="inline-details"><summary>Show</summary><code>%s</code></details>',
        text
      ))
    else
      -- For non-HTML, just show the code
      return el
    end
  end
end

-- Helper function for exercise solutions
function process_exercise_solution(blocks)
  local processed = {}
  local in_solution = false
  local solution_blocks = {}
  
  for _, block in ipairs(blocks) do
    if block.t == "Header" and pandoc.utils.stringify(block):match("Solution") then
      in_solution = true
      -- Don't include the solution header
    elseif in_solution and block.t == "Header" then
      -- End of solution section
      if #solution_blocks > 0 then
        local solution_div = pandoc.Div(solution_blocks, {class = "details"})
        solution_div.content = {
          pandoc.Header(3, "Show Solution"),
          table.unpack(solution_blocks)
        }
        table.insert(processed, Div(solution_div))
      end
      in_solution = false
      solution_blocks = {}
      table.insert(processed, block)
    elseif in_solution then
      table.insert(solution_blocks, block)
    else
      table.insert(processed, block)
    end
  end
  
  -- Handle case where solution is at the end
  if in_solution and #solution_blocks > 0 then
    local solution_div = pandoc.Div(solution_blocks, {class = "details"})
    solution_div.content = {
      pandoc.Header(3, "Show Solution"),
      table.unpack(solution_blocks)
    }
    table.insert(processed, Div(solution_div))
  end
  
  return processed
end

-- Process exercise blocks
function Pandoc(doc)
  local blocks = {}
  
  for _, block in ipairs(doc.blocks) do
    if block.t == "Div" and block.classes:includes("exercise") then
      -- Process exercise content for automatic solution hiding
      block.content = process_exercise_solution(block.content)
    end
    table.insert(blocks, block)
  end
  
  doc.blocks = blocks
  return doc
end

-- Return filter functions in order
return {
  {Pandoc = Pandoc},
  {Div = Div},
  {Code = Code}
}