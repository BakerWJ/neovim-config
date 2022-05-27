lua require('impatient')
lua require('plugins')

" Theme settings
set termguicolors
syntax enable
colorscheme tokyonight

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
set completeopt=menu,menuone,noselect

" NVIM Tree Config
nnoremap <C-j> :NvimTreeToggle <CR>
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

" LSP config (the mappings used in the default file don't quite work right)
nnoremap <silent> gd <cmd>lua vim.lsp.buf.definition()<CR>
nnoremap <silent> gD <cmd>lua vim.lsp.buf.declaration()<CR>
nnoremap <silent> gr <cmd>lua vim.lsp.buf.references()<CR>
nnoremap <silent> gi <cmd>lua vim.lsp.buf.implementation()<CR>
nnoremap <silent> K <cmd>lua vim.lsp.buf.hover()<CR>
nnoremap <leader>rn <cmd> lua vim.lsp.buf.rename()<CR>
nnoremap <silent> <C-k> <cmd>lua vim.lsp.buf.signature_help()<CR>
nnoremap <silent> <C-n> <cmd>lua vim.lsp.diagnostic.goto_prev()<CR>
nnoremap <silent> <C-p> <cmd>lua vim.lsp.diagnostic.goto_next()<CR>

" Find files using Telescope command-line sugar.
nnoremap <leader>ff <cmd>Telescope find_files<cr>
nnoremap <leader>fg <cmd>Telescope live_grep<cr>
nnoremap <leader>fb <cmd>Telescope buffers<cr>
nnoremap <leader>fh <cmd>Telescope help_tags<cr>

" Format files using LSP
nnoremap <silent> ff    <cmd>lua vim.lsp.buf.formatting_sync()<CR>

" Remove vim lsp Pattern not found at bottom
set shortmess+=c

" Vimtex
let g:vimtex_view_method = 'skim'
let g:vimtex_compiler_progname = 'nvr'

" guh
let s:current_file=expand("<sfile>")

"doge settings
let g:doge_mapping = 'mn'

let test#java#runner = 'gradletest'

" Expand
imap <expr> <CR>   vsnip#expandable()  ? '<Plug>(vsnip-expand)'         : '<C-j>'
smap <expr> <CR>   vsnip#expandable()  ? '<Plug>(vsnip-expand)'         : '<C-j>'

" Expand or jump
imap <expr> <C-l>   vsnip#available(1)  ? '<Plug>(vsnip-expand-or-jump)' : '<C-l>'
smap <expr> <C-l>   vsnip#available(1)  ? '<Plug>(vsnip-expand-or-jump)' : '<C-l>'

" Jump forward or backward
imap <expr> <Tab>   vsnip#jumpable(1)   ? '<Plug>(vsnip-jump-next)'      : '<Tab>'
smap <expr> <Tab>   vsnip#jumpable(1)   ? '<Plug>(vsnip-jump-next)'      : '<Tab>'
imap <expr> <S-Tab> vsnip#jumpable(-1)  ? '<Plug>(vsnip-jump-prev)'      : '<S-Tab>'
smap <expr> <S-Tab> vsnip#jumpable(-1)  ? '<Plug>(vsnip-jump-prev)'      : '<S-Tab>'
