# Path to your oh-my-zsh installation.
export ZSH="/home/james/.oh-my-zsh"

ZSH_THEME="robbyrussell"

# Which plugins would you like to load?
# Standard plugins can be found in $ZSH/plugins/
# Custom plugins may be added to $ZSH_CUSTOM/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git)

source $ZSH/oh-my-zsh.sh

# User configuration
alias hr="honcho run python manage.py"
alias ht="honcho run python manage.py test --verbosity 2 --parallel"
alias htk="honcho run python manage.py test --verbosity 2 --keepdb --parallel"
alias pm="docker-compose exec web python manage.py"
alias vim="nvim"
alias v="nvim"

export PATH="$HOME/.local/bin:$PATH"
export TERM="xterm-256color"
export NVM_DIR="/Users/james/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
