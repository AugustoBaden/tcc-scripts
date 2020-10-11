const axios = require("axios").default;
//dados para conectar a api parceira
const api = axios.create({
  baseURL: "URl",
  headers: { "TOKEN-KEY": "token" },
  timeout: 10000
});

module.exports = api;
