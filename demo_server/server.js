const server = require("express")()

server.get("/", (req, res)=> {
    console.log("Somebody visit this server")
    res.send("This is demo server")
})

server.post("/", (req, res) => {
    console.log("Post page using node.js")
})

server.listen(3000, () => {
    console.log("Start server on port 3000")
})
