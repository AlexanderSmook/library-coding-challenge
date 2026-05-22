FROM node:21

RUN corepack enable

WORKDIR /frontend

COPY package*.json .


# Stop Docker caching the npm install
ADD https://www.google.com /time.now

RUN npm install

COPY . .

ENV HOST="0.0.0.0"
ENV PORT=3000
EXPOSE 3000

CMD [ "npm", "run", "serve" ]
