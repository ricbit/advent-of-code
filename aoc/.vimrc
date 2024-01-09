set nocompatible
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'dense-analysis/ale'
"Plugin 'Shougo/deoplete.nvim'
"Plugin 'roxma/nvim-yarp'
"Plugin 'roxma/vim-hug-neovim-rpc'
"let g:deoplete#enable_at_startup = 1
Plugin 'file:///home/ricbit/.vim/bundle/vim-m80'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

let g:ale_linters_ignore = { 'python': ['pylint'] }
let g:ale_python_flake8_options = '--ignore=E111,F401,E302,F403,E305,E128,W293,W391,E231,E265,E303,W291,E114,E251,E501,E226,E301,E261,E262,E203,E731'
"let g:ale_lint_on_text_changed = 'always'
let g:ale_lint_delay = 100

set signcolumn=yes
set autoindent
set expandtab
autocmd InsertEnter * setlocal shiftwidth=2
autocmd InsertEnter * setlocal softtabstop=2
autocmd InsertEnter * setlocal tabstop=2

" Use tab for trigger completion with characters ahead and navigate.
" Use command ':verbose imap <tab>' to make sure tab is not mapped by other plugin.
"inoremap <expr><TAB> pumvisible() ? "\<C-n>" : "\<TAB>"
"inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

" Super Tab with Deoplete
"function! s:check_back_space() abort
"    let col = col('.') - 1
"    return !col || getline('.')[col - 1]  =~# '\s'
"endfunction

"inoremap <silent><expr> <TAB>
"     \ pumvisible() ? "\<C-n>" :
"     \ <SID>check_back_space() ? "\<Tab>" :
"     \ deoplete#manual_complete()

function! UpdateSignColumnColor(timer_id)
    if len(sign_getplaced('', {'group': '*'})[0]['signs']) > 0
        	highlight SignColumn ctermbg=white
    else
        	highlight SignColumn ctermbg=black
    endif
endfunction

"autocmd CursorMoved,CursorMovedI,InsertEnter,InsertLeave * call UpdateSignColumnColor()
let sign_timer = timer_start(200, 'UpdateSignColumnColor', {'repeat': -1})



