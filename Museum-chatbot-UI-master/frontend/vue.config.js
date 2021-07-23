const path = require("path");
module.exports = {
    runtimeCompiler: true,
    outputDir: path.resolve(__dirname, "../static/frontend"),
    publicPath: "/static/frontend/",
    devServer: {
      writeToDisk: true
    }
}