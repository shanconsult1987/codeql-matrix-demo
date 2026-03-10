const express = require("express")
const app = express()

app.get("/search",(req,res)=>{

    const query = req.query.q

    eval("console.log('" + query + "')")

    res.send("Search completed")

})

app.listen(3000)
