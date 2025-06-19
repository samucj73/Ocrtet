const API_URL = "https://api.casinoscores.com/svc-evolution-game-events/api/xxxtremelightningroulette/latest";
let historico = [];

function getColuna(numero) {
  if (numero === 0) return "Zero";
  return ((numero - 1) % 3) + 1;
}

function getLinha(numero) {
  if (numero === 0) return "Zero";
  return Math.floor((numero - 1) / 3) + 1;
}

function calcularPrevisoes() {
  const freq = {};
  historico.forEach(n => freq[n] = (freq[n] || 0) + 1);
  const numerosOrdenados = Object.entries(freq)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 4)
    .map(x => x[0]);

  const colFreq = {}, linFreq = {};
  historico.forEach(n => {
    if (n === 0) return;
    const col = getColuna(n);
    const lin = getLinha(n);
    colFreq[col] = (colFreq[col] || 0) + 1;
    linFreq[lin] = (linFreq[lin] || 0) + 1;
  });

  const colunaProvavel = Object.entries(colFreq).sort((a, b) => b[1] - a[1])[0]?.[0] || "–";
  const linhaProvavel = Object.entries(linFreq).sort((a, b) => b[1] - a[1])[0]?.[0] || "–";

  const painel = document.getElementById("previsoes");
  painel.innerHTML = `
    <strong>Números prováveis:</strong> ${numerosOrdenados.join(", ")}<br>
    <strong>Coluna provável:</strong> ${colunaProvavel}ª<br>
    <strong>Linha provável:</strong> ${linhaProvavel}
  `;
}

async function atualizar() {
  try {
    const res = await fetch(API_URL, {
      headers: { "User-Agent": "Mozilla/5.0" },
      cache: "no-store"
    });
    const data = await res.json();
    const numero = data?.data?.result?.outcome?.number;
    if (numero !== undefined && !isNaN(numero)) {
      if (historico[historico.length - 1] !== numero) {
        historico.push(numero);
        if (historico.length > 90) historico.shift();
        calcularPrevisoes();
      }
    }
  } catch (e) {
    document.getElementById("previsoes").innerText = "❌ Erro ao consultar API";
  }
}

setInterval(atualizar, 10000);
atualizar();
