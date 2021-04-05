const path = require('path');
const webpack = require('webpack');

module.exports = {
    devtool: 'source-map',
    watchOptions: {
        poll: true,
        ignored: /node_modules/
    },
    entry: {
        player: './client/src/entries/player.jsx',
    },
    resolve: {
      extensions: ['.js', '.jsx']
    },
    module: {
      rules: [
        {
          test: /.jsx?$/,
          exclude: /node_modules\/(?!(query-string|split-on-first|strict-uri-encode|ip-cidr)\/).*/,
          use: {
            loader: 'babel-loader',
            options: {
              presets: ['@babel/preset-env', '@babel/preset-react']
            }
          }
        }
      ]
    },
    optimization: {
        // runtimeChunk: true,
        splitChunks: {
            cacheGroups: {
                commons: {
                    test: /[\\/]node_modules[\\/]/,
                    minChunks: 3,
                    reuseExistingChunk: true,
                    name: "vendors",
                    chunks: "all"
                },
            }
        }
    },
    plugins: [new webpack.ProvidePlugin({})],
    output: {
      path: path.join(__dirname, './server/static/js'),
      filename: '[name].js',
      sourceMapFilename: '[name].map'
    },
    externals: {},
    node: {
      fs: 'empty'
    }
};
