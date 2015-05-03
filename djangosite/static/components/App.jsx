/**
 * @jsx React.DOM
 */


var React = require("react"),
    Search = require("./Search.jsx");

var App = React.createClass({
  render() {
    return (
      <div id="theapp">
        <div id="thesearchbox">
          <Search />
        </div>
        <div id="thecomment">
          <p>comment = {this.props.comment}</p>
        </div>
      </div>
    );
  }
});


module.exports = App;