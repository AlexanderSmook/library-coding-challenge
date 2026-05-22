FROM node:21

RUN corepack enable

WORKDIR /api

COPY package*.json .

RUN chown -R node:node /api
USER node

# Stop Docker caching the npm install
ADD https://www.google.com /time.now 
RUN npm install

COPY . .

ENV PORT=4000
EXPOSE 4000

CMD [ "npm", "start" ]
