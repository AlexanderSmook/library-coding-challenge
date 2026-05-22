FROM node:21

RUN corepack enable

WORKDIR /frontend

COPY package*.json .

RUN chown -R node:node /frontend
USER node

# Stop Docker caching the npm install
ADD https://www.google.com /time.now 
RUN npm install

COPY . .

ENV PORT=3000
EXPOSE 3000

CMD [ "npm", "start" ]
