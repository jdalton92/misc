" ------------------------------------ Sets ------------------------------------
" Enable syntax highlighting
syntax on
" Encoding displayed
set encoding=utf-8
" Enable mouse
set mouse=a
" Copy/paste between vim and clipboard
set clipboard=unnamedplus
" Auto source config files
set exrc
" Line numbers are relative
set relativenumber
" Show current line number
set nu
" Incremental highlighting when searching
set incsearch
" No highlighting after search complete
set nohlsearch
" Keep buffers when unloaded
set hidden
" No error sounds
set noerrorbells
" Tab config
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
" Stop newline continuation of comments
set formatoptions-=cro
" Stop text wrapping
set nowrap
" Case insensitive search
set ignorecase
" File history config
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
" Move window when scrolling page
set scrolloff=10
" Column at 81 chars
set colorcolumn=81
" Allow extra LHS column for errors etc.
set signcolumn=yes
" Give more space for displaying messages
set cmdheight=2
" Shorter update time (default=4000ms)
set updatetime=200
" Horizontal splits will be below
set splitbelow
" Veritcal splits will be to the right
set splitright
" Highlight current line
set cursorline
" LHS status line
set statusline=
set statusline+=\ %M " Indicate if changes made
set statusline+=\ %y " Display file type
set statusline+=\ %F " Show full file path
" RHS status line
set statusline+=%=
set statusline+=\ %l/%L " line/Total lines
set statusline+=\ [%n] " Buffer number

" ----------------------------- Plugins (vim-plugged) --------------------------
call plug#begin('~/.vim/plugged')

" Fuzzy finder with file previews
Plug 'nvim-lua/plenary.nvim'
Plug 'nvim-telescope/telescope.nvim'
" Color theme
Plug 'morhetz/gruvbox'
" Treesitter parser generator tool
Plug 'nvim-treesitter/nvim-treesitter', {'do': ':TSUpdate'}
" LSP
Plug 'neovim/nvim-lspconfig'

call plug#end()

" Set colorscheme
colorscheme gruvbox

" ----------------------------- Remaps -----------------------------------------
let mapleader = " "
map <C-s> :source ~/.config/nvim/init.vim<CR>
" Telescope mapping
    " Search files for word
    nnoremap <leader>ps :lua require('telescope.builtin').grep_string({ search = vim.fn.input("Grep for > ")})<CR>
    " Find files using Telescope command-line sugar.
    nnoremap <leader>ff <cmd>Telescope find_files<cr>
    nnoremap <leader>fg <cmd>Telescope live_grep<cr>
    nnoremap <leader>fb <cmd>Telescope buffers<cr>
    nnoremap <leader>fh <cmd>Telescope help_tags<cr>
    " Using Lua functions
    nnoremap <leader>ff <cmd>lua require('telescope.builtin').find_files()<cr>
    nnoremap <leader>fg <cmd>lua require('telescope.builtin').live_grep()<cr>
    nnoremap <leader>fb <cmd>lua require('telescope.builtin').buffers()<cr>
    nnoremap <leader>fh <cmd>lua require('telescope.builtin').help_tags()<cr>
" Resize splits
nnoremap <leader><Up> :resize +2<CR>
nnoremap <leader><Down> :resize -2<CR>
nnoremap <leader><Left> :vertical resize +2<CR>
nnoremap <leader><Right> :vertical resize -2<CR>
" Move between splts
nnoremap <C-Left> <C-W>h
nnoremap <C-h> <C-W>h
nnoremap <C-Down> <C-W>j
nnoremap <C-j> <C-W>j
nnoremap <C-Up> <C-W>k
nnoremap <C-k> <C-W>k
nnoremap <C-Right> <C-W>l
nnoremap <C-l> <C-W>l
" Keep highlighted section after tabbing
vnoremap < <gv
vnoremap > >gv

" ----------------------------- Autocommand ------------------------------------
" Trim whitespace
fun! TrimWhitespace()
    let l:save = winsaveview()
    keeppatterns %s/\s\+$//e
    call winrestview(l:save)
endfun

" Clear listeners so sourcing does not duplicate listeners
augroup JD_VIMRC
    autocmd!
    autocmd BufWritePre * :call TrimWhitespace()
augroup END

