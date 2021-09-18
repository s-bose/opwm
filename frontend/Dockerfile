FROM node:lts-alpine

RUN npm install -g serve

WORKDIR /frontend

ENV PATH /frontend/node_modules/.bin:$PATH

COPY package.json .
COPY package-lock.json .

RUN npm install

COPY . /frontend/

RUN npm run build

EXPOSE 3333
