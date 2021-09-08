call plug#begin()
" Plugins
" Theme + Lualine
Plug 'folke/tokyonight.nvim'
Plug 'romgrk/barbar.nvim'
Plug 'hoob3rt/lualine.nvim'
" File Explorer
Plug 'kyazdani42/nvim-tree.lua'
Plug 'tiagofumo/vim-nerdtree-syntax-highlight'
" Icons
Plug 'kyazdani42/nvim-web-devicons'
Plug 'ryanoasis/vim-devicons'
" Commenting
Plug 'b3nj5m1n/kommentary'
" Latex
Plug 'lervag/vimtex'
" Git plugin
Plug 'tpope/vim-fugitive'
" See edited lines from git
Plug 'airblade/vim-gitgutter'
" Opening page
Plug 'mhinz/vim-startify'
" LSP support
Plug 'neovim/nvim-lspconfig'
Plug 'hrsh7th/nvim-compe'
Plug 'sheerun/vim-polyglot'
" Telescope
Plug 'nvim-lua/popup.nvim'
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'
" Autopairs
Plug 'windwp/nvim-autopairs'
" Autotag
Plug 'windwp/nvim-ts-autotag'
" Treesitter
Plug 'nvim-treesitter/nvim-treesitter', {'branch': '0.5-compat','do': ':TSUpdate'}
" Discord flex
Plug 'andweeb/presence.nvim'
" Colorizer
Plug 'norcalli/nvim-colorizer.lua'
" Todo Commenter
Plug 'folke/todo-comments.nvim'
" Snippets
Plug 'hrsh7th/vim-vsnip'
Plug 'hrsh7th/vim-vsnip-integ'
Plug 'rafamadriz/friendly-snippets'
" Find and replace
Plug 'windwp/nvim-spectre'
" Java plugin
Plug 'mfussenegger/nvim-jdtls'
" Fterm
Plug 'numtostr/FTerm.nvim'
call plug#end()

" Config section

" Theme settings
set termguicolors
syntax enable
colorscheme tokyonight

" Add lua config
lua require('config')

" Basic settings
scriptencoding utf-8
set encoding=utf-8
set number relativenumber
set ignorecase
set smartcase
set noswapfile
set nohlsearch
set autoread
set mouse=a
set t_Co=256
set expandtab
set autoindent
set noshowmode
set showtabline=2
set hidden
" Remap esc key
inoremap jk <ESC>
" Remap leader
let mapleader = " "
" Use system clipboard
set clipboard=unnamedplus
" Keep lines visible when scrolling
set scrolloff=7
" Allow filetype checking
filetype plugin indent on
" Remove i from autocomplete
set complete-=i
set incsearch
" autocomplete for command line
set wildmenu
" check if file has been changed
set autoread
" increase history length
set history=1000
" compe completion
set completeopt=menuone,noselect
highlight link CompeDocumentation NormalFloat

" NVIM Tree Config
nnoremap <C-j> :NvimTreeToggle <CR>
let g:nvim_tree_ignore = ['.git', '.cache', '.DS_Store', '__pycache__']
let g:nvim_tree_quit_on_open = 1
let g:nvim_tree_indent_markers = 1
let g:nvim_tree_icon_padding = '  '
let g:nvim_tree_git_hl = 1

let g:nvim_tree_icons = {
    \ 'default': '',
    \ 'symlink': '',
    \ 'folder': {
    \   'arrow_open': "",
    \   'arrow_closed': "",
    \   'default': "",
    \   'open': "",
    \   'empty': "",
    \   'empty_open': "",
    \   'symlink': "",
    \   'symlink_open': "",
    \   },
    \ }

let g:nvim_tree_show_icons = {
    \ 'git': 0,
    \ 'folders': 1,
    \ 'files': 1,
    \ 'folder_arrows': 1,
    \ }

" NERD Commenter
let g:NERDCreateDefaultMappings = 1
let g:NERDSpaceDelims = 1
let g:NERDCompactSexyComs = 1
let g:NERDDefaultAlign = 'left'
let g:NERDTrimTrailingWhitespace = 1

" Compe bindings
inoremap <silent><expr> <C-Space> compe#complete()
inoremap <silent><expr> <CR>      compe#confirm(luaeval("require 'nvim-autopairs'.autopairs_cr()"))
inoremap <silent><expr> <C-e>     compe#close('<C-e>')
inoremap <silent><expr> <C-f>     compe#scroll({ 'delta': +4 })
inoremap <silent><expr> <C-d>     compe#scroll({ 'delta': -4 })

" LSP config (the mappings used in the default file don't quite work right)
nnoremap <silent> gd <cmd>lua vim.lsp.buf.definition()<CR>
nnoremap <silent> gD <cmd>lua vim.lsp.buf.declaration()<CR>
nnoremap <silent> gr <cmd>lua vim.lsp.buf.references()<CR>
nnoremap <silent> gi <cmd>lua vim.lsp.buf.implementation()<CR>
nnoremap <silent> K <cmd>lua vim.lsp.buf.hover()<CR>
nnoremap <silent> <C-k> <cmd>lua vim.lsp.buf.signature_help()<CR>
nnoremap <silent> <C-n> <cmd>lua vim.lsp.diagnostic.goto_prev()<CR>
nnoremap <silent> <C-p> <cmd>lua vim.lsp.diagnostic.goto_next()<CR>

" Find files using Telescope command-line sugar.
nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>

" Format files using LSP
nnoremap <silent> ff    <cmd>lua vim.lsp.buf.formatting()<CR>

" Remove vim lsp Pattern not found at bottom
set shortmess+=c

" vim-vsnip settings
" Expand
imap <expr> <C-j>   vsnip#expandable()  ? '<Plug>(vsnip-expand)'         : '<C-j>'
smap <expr> <C-j>   vsnip#expandable()  ? '<Plug>(vsnip-expand)'         : '<C-j>'

" Expand or jump
imap <expr> <C-l>   vsnip#available(1)  ? '<Plug>(vsnip-expand-or-jump)' : '<C-l>'
smap <expr> <C-l>   vsnip#available(1)  ? '<Plug>(vsnip-expand-or-jump)' : '<C-l>'

" Jump forward or backward
" imap <expr> <Tab>   vsnip#jumpable(1)   ? '<Plug>(vsnip-jump-next)'      : '<Tab>'
" smap <expr> <Tab>   vsnip#jumpable(1)   ? '<Plug>(vsnip-jump-next)'      : '<Tab>'
" imap <expr> <S-Tab> vsnip#jumpable(-1)  ? '<Plug>(vsnip-jump-prev)'      : '<S-Tab>'
" smap <expr> <S-Tab> vsnip#jumpable(-1)  ? '<Plug>(vsnip-jump-prev)'      : '<S-Tab>'

" Select or cut text to use as $TM_SELECTED_TEXT in the next snippet.
" See https://github.com/hrsh7th/vim-vsnip/pull/50
nmap        s   <Plug>(vsnip-select-text)
xmap        s   <Plug>(vsnip-select-text)
nmap        S   <Plug>(vsnip-cut-text)
xmap        S   <Plug>(vsnip-cut-text)

" Vimtex
let g:vimtex_view_method = 'skim'
let g:vimtex_compiler_progname = 'nvr'

" spectre
nnoremap <leader>S :lua require('spectre').open()<CR>
"search current word
nnoremap <leader>sw :lua require('spectre').open_visual({select_word=true})<CR>
vnoremap <leader>s :lua require('spectre').open_visual()<CR>
"  search in current file
nnoremap <leader>sp viw:lua require('spectre').open_file_search()<cr>

" java setup
if has('nvim-0.5')
  augroup lsp
    au!
    au FileType java lua require('jdtls').start_or_attach({cmd = {'java-lsp.sh'}})
  augroup end
endif