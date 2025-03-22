const http = require('http');

const PORT = process.env.PORT || 3000;
const server = http.createServer((req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end(`Servidor funcionando en el puerto ${PORT}\n`);
});

server.listen(PORT, () => {
    console.log(`Servidor en ejecución en el puerto ${PORT}`);
});