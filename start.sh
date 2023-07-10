if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/soxgsvzztafah/Tele-AiBot.git /Tele-AiBot
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Tele-AiBot
fi
cd /Tele-AiBot
pip3 install -U -r requirements.txt
echo "Starting 😇Telegram AI BOT😇...."
python3 tele-bot.py