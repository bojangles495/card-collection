const Fs = require('fs')
const HtmlWebpackPlugin = require('html-webpack-plugin')
const MiniCssExtractPlugin = require('mini-css-extract-plugin')
const OptimizeCssAssetsPlugin = require('optimize-css-assets-webpack-plugin')
const Path = require('path')
const UglifyJsPlugin = require('uglifyjs-webpack-plugin')
const Webpack = require('webpack')
const WebpackManifestPlugin = require('webpack-manifest-plugin')

const hashDigest = 'hex'
const hashDigestLength = 20
const hashFunction = 'sha384'

class CleanPlugin {
  apply(compiler) {
    compiler.hooks.afterEmit.tap('CleanPlugin', compilation => {
      if (0 === compilation.errors.length) {
        Fs.readdir(compilation.options.output.path, (err, files) => {
          if (err) {
            console.log(`failed to read directory: ${compilation.options.output.path}:`, err)
          } else {
            files.forEach(file => {
              if (!compilation.assets.hasOwnProperty(file)) {
                const path = Path.resolve(compilation.options.output.path, file)
                Fs.unlink(path, err => {
                  if (err) {
                    console.log(`failed to unlink file: ${path}:`, err)
                  }
                })
              }
            })
          }
        })
      }
    })
  }
}

const topdir = __dirname
const baseConfig =
  { context: Path.resolve(topdir, 'front_end')
  , entry:
    { 'index':
      [ './javascript/index.js'
      , './sass/index.scss'
      ]
    }
  , mode: 'development' // The `--mode` argument overrides this.
  , output:
    { path: Path.resolve(topdir, 'obj')
    , filename: '[name].[chunkhash].js'
    , hashDigest
    , hashDigestLength
    , hashFunction
    }
  , plugins:
    [ new CleanPlugin()
    , new MiniCssExtractPlugin
      ( { filename: '[name].[chunkhash].css'
        }
      )
    , new HtmlWebpackPlugin
      ( { template: Path.resolve(topdir, 'front_end', 'html', 'index.ejs')
        , minify: true
        }
      )
    , new WebpackManifestPlugin()
    ]
  , module:
    { rules:
      [ { test: /\.css$/
        , use:
          [ MiniCssExtractPlugin.loader
          , 'css-loader'
          ]
        }
      , { test: /\.eot$|\.svg$|\.ttf$|\.png|\.jpg|\.woff2?$/
        , use:
          { loader: 'file-loader'
          , query:
            { name: '[name].[ext]'
            }
          }
        }
      , { test: /\.m?js$/
        , exclude: /(node_modules|bower_components)/
        , use:
          { loader: 'babel-loader'
          }
        }
      , { use:
          [ { loader: 'style-loader'
            }
          , { loader: 'css-loader'
            }
          , { loader: 'sass-loader'
            }
          ]
        , test: /\.scss$/
        }
      ]
    }
  , resolve: 
      { extensions:
          [ '.js'
          , '.scss'
          , '.svg'
          ]
      , modules:
          [ Path.resolve(topdir, 'front_end', 'javascript')
          , Path.resolve(topdir, 'node_modules')
          ]
      }
  , optimization:
    { minimizer:
      [ new OptimizeCssAssetsPlugin()
      ]
    , splitChunks:
      { cacheGroups:
        { client:
          { test: /[\\/]javascript[\\/]/
          , name: 'javascript'
          , chunks: 'all'
          }
        , vendor:
          { test: /[\\/]node_modules[\\/]/
          , name: 'vendor'
          , chunks: 'all'
          }
        }
      }
    }
  , watchOptions:
    { ignored: /\.sw.$/
    }
  , devServer:
    { contentBase: Path.resolve(topdir, 'front_end', 'main', 'html')
    , historyApiFallback: true
    , disableHostCheck: true
    , headers:
      { 'Access-Control-Allow-Origin': '*'
      }
    , proxy:
      { '/api':
          { 
            target: 'http://flask:3011'
          // target: 'http://localhost:5000'
          , secure: false
          , changeOrigin: true
          }
      }
    , watchOptions:
      { ignored: /\.sw.$/
      , poll: true
      }
    }
  }

module.exports = (env, argv) => {
  let config
  if (argv.mode !== 'production') {
    config =
      { ...baseConfig
      , devtool: 'cheap-module-source-map'
      }
  } else {
    config =
      { ...baseConfig
      , devtool: 'source-map'
      , optimization:
        { ...baseConfig.optimization
        , minimizer:
          [ ...baseConfig.optimization.minimizer
          , new UglifyJsPlugin
            ( { sourceMap: false
              , uglifyOptions:
                { compress: true
                }
              }
            )
          ]
        }
      }
  }
  return config
}
