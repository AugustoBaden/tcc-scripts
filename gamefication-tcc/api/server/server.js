const express = require("express");
const apiRouter = require("./routes");
var cors = require("cors");

const app = express();

app.use(express.json());
app.use(cors());
//use gamefication?
app.use("/api/gamefication", apiRouter);

// if you want to deploy
//tutorial says 3000, mariadb is on 3306 127.0.0.1
app.listen(process.env.PORT || "3001", () => {
  console.log(`Server is running on port: ${process.env.PORT || "3001"}`);
});
