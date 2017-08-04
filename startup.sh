docker run -d -p 4445:4444 selenium/standalone-chrome
docker run -d -p 4446:4444 selenium/standalone-chrome-local

docker run -d -p 4447:4444 selenium/standalone-chrome-debug

docker build -t selenium/standalone-chrome-local .
