return require("packer").startup(function()
	use("wbthomason/packer.nvim")
	-- theme + lualine
	use("folke/tokyonight.nvim")
	use({
		"romgrk/barbar.nvim",
		requires = { "kyazdani42/nvim-web-devicons" },
	})
	use({
		"hoob3rt/lualine.nvim",
		requires = { "kyazdani42/nvim-web-devicons", opt = true },
	})
	-- File explorer
	use({
		"kyazdani42/nvim-tree.lua",
		requires = "kyazdani42/nvim-web-devicons",
	})
	-- Commenting
	use("b3nj5m1n/kommentary")
	-- Latex
	use("lervag/vimtex")
	-- Git plugins
	use({
		"lewis6991/gitsigns.nvim",
		requires = {
			"nvim-lua/plenary.nvim",
		},
	})
	-- Opening page
	use("mhinz/vim-startify")
	-- nvim-cmp
	use("hrsh7th/cmp-nvim-lsp")
	use("hrsh7th/cmp-buffer")
	use("hrsh7th/cmp-path")
	use("hrsh7th/nvim-cmp")
	use("hrsh7th/cmp-vsnip")
	-- snippets
	use("hrsh7th/vim-vsnip")
	use("rafamadriz/friendly-snippets")
	-- LSP support
	use("neovim/nvim-lspconfig")
	use("williamboman/nvim-lsp-installer")
	use("jose-elias-alvarez/null-ls.nvim")
	-- Telescope
	use({
		"nvim-telescope/telescope.nvim",
		requires = { { "nvim-lua/plenary.nvim" } },
	})
	-- Autopairs
	use("windwp/nvim-autopairs")
	-- Autotag
	use("windwp/nvim-ts-autotag")
	-- Treesitter
	use({
		"nvim-treesitter/nvim-treesitter",
		run = ":TSUpdate",
	})
	-- Todo Commenter
	use({
		"folke/todo-comments.nvim",
		requires = "nvim-lua/plenary.nvim",
	})
	-- Colorizer
	use("norcalli/nvim-colorizer.lua")
	-- Java plugin
	use("mfussenegger/nvim-jdtls")
	-- Lightspeed
	use("ggandor/lightspeed.nvim")
	-- Nvim DAP
	use("mfussenegger/nvim-dap")
	use({ "rcarriga/nvim-dap-ui", requires = { "mfussenegger/nvim-dap" } })
	-- Glow
	use({ "ellisonleao/glow.nvim" })
	-- documentation
	use({
		"kkoomen/vim-doge",
		run = ":call doge#install()",
	})
	-- testing
	use("vim-test/vim-test")
	use("tpope/vim-sleuth")
end)
