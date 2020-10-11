const mysql = require("mysql");

// pool allows make call as query, managing a list of connections
const pool = mysql.createPool({
  connectionLimit: 100,
  password: "password",
  user: "user",
  database: "database",
  host: "host",
  port: "port"
});

const gameficationdb = {};

gameficationdb.all = () => {
  return new Promise((resolve, reject) => {
    pool.query(`SELECT * FROM Atividade`, (err, results) => {
      if (err) {
        return reject(err);
      }
      return resolve(results);
    });
  });
};

gameficationdb.one = CPF => {
  // console.log(CPF);
  return new Promise((resolve, reject) => {
    pool.query(
      `SELECT ContextoEv, pontos, contagem as qntVezes, eventokey  FROM resultado where CPF = ?`,
      [CPF],
      (err, results) => {
        if (err) {
          return reject(err);
        }
        const objetos = {};
        let soma = 0;
        let somaQntdVezes = 0;
        results.map(async cat => {
          soma += cat.pontos;
          somaQntdVezes += cat.qntVezes;
          const key = cat.eventokey;

          // remove a chave do que vai tertornar
          const { eventokey, ...catresult } = cat;
          objetos[key] = { ...catresult };
          // return {...cat,soma}
        });
        objetos.soma = soma;
        objetos.somaQntdVezes = somaQntdVezes;
        // console.log(ob);

        return resolve(objetos);
      }
    );
  });
};
gameficationdb.desafios = CPF => {
  // console.log(CPF);
  return new Promise((resolve, reject) => {
    pool.query(
      `SELECT contagem, eventokey  FROM resultado where CPF = ?`,
      [CPF],
      (err, results) => {
        if (err) {
          return reject(err);
        }
        const objetos = {};
        let somaQntdVezes = 0;
        // monta o objeto que vai ser devolvido para o usuario
        results.map(async cat => {
          const { eventokey, contagem } = cat;
          // faz a soma de todas as atividades que o usuario fez no sistema
          if (eventokey) {
            somaQntdVezes += cat.contagem;
            objetos[eventokey] = contagem;
          }
        });
        // adiciona a soma ao objeto que será devolvido
        if (!objetos === {}) {
          objetos.somaQntdVezes = somaQntdVezes;
        }
        return resolve(objetos);
      }
    );
  });
};

// subquery voltada pra obter dados do ranking
gameficationdb.estado = CPF => {
  return new Promise((resolve, reject) => {
    pool.query(
      `SELECT NomeAlu, RA, ContextoEv, contagem , idEstado , polo, curso FROM resultado where idEstado = ( select MAX(idEstado) from resultado where CPF = ?) Group by ContextoEv, RA, NomeAlu,contagem,idEstado ,polo,curso order by contagem desc`,
      [CPF],
      (err, results) => {
        if (err) {
          return reject(err);
        }
        return resolve(results);
      }
    );
  });
};

gameficationdb.estadonum = RA => {
  return new Promise((resolve, reject) => {
    pool.query(
      `SELECT NomeAlu, RA, ContextoEv, contagem FROM resultado where sigEstado = ( select MAX(sigEstado) from resultado where RA = ?) group by NomeAlu order by contagem desc`,
      [RA],
      (err, results) => {
        if (err) {
          return reject(err);
        }
        return resolve(results);
      }
    );
  });
};

// em construção
// rankings
// ranking Estado
gameficationdb.rankingEstado = estado => {
  return new Promise((resolve, reject) => {
    pool.query(
      `SELECT p.RA, p.totalPontos,polo, curso, @curRank := @curRank + 1 AS positionRanking  FROM rankings p, (SELECT @curRank := 0) r  where CPF is not null and RA is not null and p.idEstado = ? ORDER BY totalPontos DESC ;`,
      [estado],
      (err, results) => {
        err ? reject(err) : resolve(results); // eslint-disable-line
      }
    );
  });
};

// ranking geral
gameficationdb.hankingAll = () => {
  return new Promise((resolve, reject) => {
    pool.query(
      `SELECT RA, totalPontos, polo, curso, @curRank := @curRank + 1 AS positionRanking  FROM rankings p, (SELECT @curRank := 0) r  where CPF is not null and RA is not null ORDER BY totalPontos DESC ;`,
      (err, results) => {
        err ? reject(err) : resolve(results); // eslint-disable-line
      }
    );
  });
};
// ranking Polo
gameficationdb.rankingPolo = nomePolo => {
  const polo = `%${nomePolo}%`;
  return new Promise((resolve, reject) => {
    pool.query(
      "SELECT RA, totalPontos, polo, curso, @curRank := @curRank + 1 AS positionRanking FROM rankings r, (SELECT @curRank := 0) cr where CPF is not null and RA is not null and polo LIKE ? ORDER BY totalPontos DESC;",
      [polo],
      (err, results) => {
        err ? reject(err) : resolve(results); // eslint-disable-line
      }
    );
  });
};
// ranking Curso
gameficationdb.rankingCurso = curso => {
  return new Promise((resolve, reject) => {
    pool.query(
      `SELECT RA, totalPontos, polo, curso, @curRank := @curRank + 1 AS positionRanking FROM rankings r, (SELECT @curRank := 0) cr where CPF is not null and RA is not null and curso = ? ORDER BY totalPontos DESC;`,
      [curso],
      (err, results) => {
        err ? reject(err) : resolve(results); // eslint-disable-line
      }
    );
  });
};
// ranking Polo Curso
gameficationdb.rankingPoloCurso = (polo, curso) => {
  return new Promise((resolve, reject) => {
    pool.query(
      `SELECT RA, totalPontos, polo, curso, @curRank := @curRank + 1 AS positionRanking FROM rankings r, (SELECT @curRank := 0) cr where CPF is not null and RA is not null and polo = ? and curso = ? ORDER BY totalPontos DESC;`,
      [polo, curso],
      (err, results) => {
        err ? reject(err) : resolve(results); // eslint-disable-line
      }
    );
  });
};
module.exports = gameficationdb;
