const express = require("express");
const db = require("../db");
const api = require("../../config/axios");

const router = express.Router();

router.get("/", async (req, res) => {
  try {
    const results = await db.all();
    res.json(results);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }

  // res.json({ test: 'test' });
});

router.get("/:logsId", async (req, res) => {
  try {
    const results = await db.one(req.params.logsId);
    res.json(results);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});

router.post("/js", async (req, res) => {
  try {
    const { CPF } = req.body;
    let results = await db.one(CPF);
    if (results.soma === 0) {
      results = { erro: "Você ainda não pontuou" };
    }
    res.json(results);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});

router.post("/check", async (req, res) => {
  try {
    const { password, user } = req.body;

    const { data } = await api.post("/check_external", `user=${user}&password=${password}`);

    res.send(data);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});
router.post("/profile", async (req, res) => {
  try {
    const { id } = req.body;

    const { data } = await api.post("/profile_external", `id=${id}`);

    res.send(data);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});
router.post("/desafios", async (req, res) => {
  try {
    const { CPF } = req.body;
    let results = await db.desafios(CPF);

    if (results.soma === 0 || JSON.stringify(results).length === 2) {
      results = { erro: "Você ainda não pontuou" };
    }
    res.json(results);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});

router.post("/estado", async (req, res) => {
  try {
    const { CPF } = req.body;
    const results = await db.estado(CPF);
    res.json(results);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});

router.post("/estadonum", async (req, res) => {
  try {
    const { RA } = req.body;
    const results = await db.estadonum(RA);
    res.json(results);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});
router.post("/ranking", async (req, res) => {
  try {
    const { ESTADO } = req.body;
    const results = await db.ranking(ESTADO);
    res.json(results);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});
router.post("/rankingAll", async (req, res) => {
  try {
    // const { ESTADO } = req.body;
    const results = await db.hankingAll();
    res.json(results);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});
router.post("/rankingEstado", async (req, res) => {
  try {
    let { ESTADO } = req.body;
    const results = await db.rankingEstado(ESTADO);
    res.json(results);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});
router.post("/rankingPolo", async (req, res) => {
  try {
    let { polo } = req.body;
    const results = await db.rankingPolo(polo);
    res.json(results);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});
router.post("/rankingCurso", async (req, res) => {
  try {
    let { curso } = req.body;
    const results = await db.rankingCurso(curso);
    res.json(results);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});
router.post("/rankingPoloCurso", async (req, res) => {
  try {
    let { polo, curso } = req.body;
    const results = await db.rankingPoloCurso(polo, curso);
    res.json(results);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});
router.post("/teste", async (req, res) => {
  try {
    const results = await db.testes();
    res.json(results);
  } catch (e) {
    console.log(e); // eslint-disable-line
    res.sendStatus(500);
  }
});

module.exports = router;
