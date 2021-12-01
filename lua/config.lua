require('lualine').setup {
  options = {
    theme = 'tokyonight',
  },
}

require'nvim-web-devicons'.setup {
 -- your personnal icons can go here (to override)
 -- DevIcon will be appended to `name`
 override = {
  zsh = {
    icon = "",
    color = "#428850",
    name = "Zsh"
  }
 };
 -- globally enable default icons (default to false)
 -- will get overriden by `get_icons` option
 default = true;
}

-- Treesitter setup
require'nvim-treesitter.configs'.setup {
  highlight = {
    enable = true,
  },
  incremental_selection = {
    enable=true
  },
  -- use nvim-ts-autotags
  autotag = {
    enable = true,
  }
}

-- LSP Setup

local lsp_installer = require("nvim-lsp-installer")

local capabilities = vim.lsp.protocol.make_client_capabilities()
capabilities.textDocument.completion.completionItem.snippetSupport = true

local flake8 = {
    lintCommand = "flake8 --max-line-length 88 --format '%(path)s:%(row)d:%(col)d: %(code)s %(code)s %(text)s' --stdin-display-name ${INPUT} -",
    lintStdin = true,
    lintIgnoreExitCode = true,
    lintFormats = {"%f:%l:%c: %t%n%n%n %m"},
    lintSource = "flake8"
}

local black = {
  formatCommand = "black -",
  formatStdin = true
}

local isort = {
  formatcommand = "isort --stdout --profile black -",
  formatStdin = true
}

local prettier = {
  formatCommand = "prettier --stdin-filepath ${INPUT}",
  formatStdin = true
}

-- Register a handler that will be called for all installed servers.
-- Alternatively, you may also register handlers on specific server instances instead (see example below).
lsp_installer.on_server_ready(function(server)
    local opts = {}

    if server.name == 'pyright' then
      opts.settings = {
        python = {
          analysis = {
            stubPath = '/Users/bakerwjackson/.config/nvim/typings/'
          }
      }}
    end

    if server.name == 'cssls' then
      opts.capabilities = capabilities
    end

    if server.name == 'html' then
      opts.capabilities = capabilities
    end

    if server.name == 'efm' then
      opts.init_options = {documentFormatting = true}
      opts.filetypes = {"python", "javascript", "javascriptreact",
                        "typescript", "typescriptreact", "html",
                        "css", "json", "yaml"}
      opts.settings = {
        languages = {
          python = {flake8, black, isort},
          javascript = {prettier},
          javascriptreact = {prettier},
          typescript = {prettier},
          typescriptreact = {prettier},
          html = {prettier},
          css = {prettier},
          json = {prettier},
          yaml = {prettier},
        }
      }
    end

    if server.name ~= 'jdtls' then
      server:setup(opts)
    end
end)

local t = function(str)
  return vim.api.nvim_replace_termcodes(str, true, true, true)
end

local check_back_space = function()
    local col = vim.fn.col('.') - 1
    if col == 0 or vim.fn.getline('.'):sub(col, col):match('%s') then
        return true
    else
        return false
    end
end


vim.api.nvim_set_keymap("i", "<Tab>", "v:lua.tab_complete()", {expr = true})
vim.api.nvim_set_keymap("s", "<Tab>", "v:lua.tab_complete()", {expr = true})
vim.api.nvim_set_keymap("i", "<S-Tab>", "v:lua.s_tab_complete()", {expr = true})
vim.api.nvim_set_keymap("s", "<S-Tab>", "v:lua.s_tab_complete()", {expr = true})

-- autopairs config
require('nvim-autopairs').setup()

local remap = vim.api.nvim_set_keymap

-- skip it, if you use another global object
_G.MUtils= {}

remap('i' , '<CR>','v:lua.MUtils.completion_confirm()', {expr = true , noremap = true})

-- Neovim colorizer
require'colorizer'.setup()

require"todo-comments".setup{}

-- Change completion icons
require('vim.lsp.protocol').CompletionItemKind = {
    '', -- Text
    '', -- Method
    '', -- Function
    '', -- Constructor
    '', -- Field
    '', -- Variable
    '', -- Class
    'ﰮ', -- Interface
    '', -- Module
    '', -- Property
    '', -- Unit
    '', -- Value
    '了', -- Enum
    '', -- Keyword
    '﬌', -- Snippet
    '', -- Color
    '', -- File
    '', -- Reference
    '', -- Folder
    '', -- EnumMember
    '', -- Constant
    '', -- Struct
    '', -- Event
    'ﬦ', -- Operator
    '', -- TypeParameter
}

require('gitsigns').setup()

require'nvim-tree'.setup{
  hijack_cursor = true,
  git = {enable = false, ignore=true},
  filters = {custom={'.git', '.idea', '.cache', '.DS_Store', '__pycache__'}}
}

require('coq')

vim.g.glow_binary_path = "/usr/local/bin"
