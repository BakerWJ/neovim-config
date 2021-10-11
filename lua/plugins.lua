return require('packer').startup(function()
  use 'wbthomason/packer.nvim'
  -- theme + lualine
  use 'folke/tokyonight.nvim'
  use {
    'romgrk/barbar.nvim',
    requires = {'kyazdani42/nvim-web-devicons'}
  }
  use {
    'hoob3rt/lualine.nvim',
    requires = {'kyazdani42/nvim-web-devicons', opt = true}
  }
  -- File explorer
  use {
    'kyazdani42/nvim-tree.lua',
    requires = 'kyazdani42/nvim-web-devicons'
  }
  -- Commenting
  use 'b3nj5m1n/kommentary'
  -- Latex
  use 'lervag/vimtex'
  -- Git plugins
  use {
    'lewis6991/gitsigns.nvim',
    requires = {
      'nvim-lua/plenary.nvim'
    }
  }
  -- Opening page
  use 'mhinz/vim-startify'
  -- LSP support
  use 'hrsh7th/nvim-compe'
  use 'sheerun/vim-polyglot'
  use 'neovim/nvim-lspconfig'
  -- Telescope
  use {
    'nvim-telescope/telescope.nvim',
    requires = { {'nvim-lua/plenary.nvim'} }
  }
  -- Autopairs
  use 'windwp/nvim-autopairs'
  -- Autotag
  use 'windwp/nvim-ts-autotag'
  -- Treesitter
  use {
    'nvim-treesitter/nvim-treesitter',
    run = ':TSUpdate'
  }
  -- Todo Commenter
  use {
    "folke/todo-comments.nvim",
    requires = "nvim-lua/plenary.nvim",
  }
  -- Colorizer
  use 'norcalli/nvim-colorizer.lua'
  -- Snippets
  use 'hrsh7th/vim-vsnip'
  use 'hrsh7th/vim-vsnip-integ'
  use 'rafamadriz/friendly-snippets'
  -- Java plugin
  use 'mfussenegger/nvim-jdtls'
  -- Fterm
  use "numtostr/FTerm.nvim"
  -- Lightspeed
  use 'ggandor/lightspeed.nvim'
  -- Nvim DAP
  use 'mfussenegger/nvim-dap'
  use { "rcarriga/nvim-dap-ui", requires = {"mfussenegger/nvim-dap"} }
  -- Code runner
  use 'pianocomposer321/yabs.nvim'
end)
