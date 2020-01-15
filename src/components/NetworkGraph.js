import React, { Component } from 'react';
import * as d3 from 'd3';
import PropTypes from 'prop-types';
import './NetworkGraph.css';


class NetworkGraph extends Component {

  componentDidMount() {
    if (!this.props.data.ing_data) {
      return
    }
    this.drawGraph(this.props.data);
  }

  componentDidUpdate() {
    if (!this.props.data.ing_data) {
      return
    }
    this.drawGraph(this.props.data);
  }

  drawGraph(data) {
    if (!data.ing_data) {
      return
    }
    const { ing_data } = data
    console.log(ing_data[0]);
    const nodes = [{"id": ing_data[0].source_id, "name": ing_data[0].source_name, "strength": 1}, ...ing_data.map(r => {
      return {
        "id": r.target_id,
        "name": r.target,
        "strength": r.strength
      }})];
    const links = ing_data.map(r => {
      return {
        "source": r.source_id,
        "target": r.target_id,
        "strength": r.strength
      }});

    const svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height")
    // const padding = "5";

    const simulation = d3.forceSimulation()
    .nodes(nodes);

    simulation
      .force("charge_force", d3.forceManyBody().strength(-3000))
      .force("center_force", d3.forceCenter(width / 2, height / 2))

    const group = d3.select(this.refs.links)
    const group2 = d3.select(this.refs.nodes)

    const node = group2
      .attr("class", "nodes")
      .selectAll("circle")
      .data(nodes)
      .enter()
      .append("circle")
      // .attr("width", width - padding )
      // .attr("height", height - padding)
      .attr("r", circleSize)
      .attr("fill", circleColor)
      .style("opacity", circleOpacity)
      .style("stroke", 'black')
      .on('mouseover', function(d) {
        if(d !== nodes[0]){
          d3.select(this)
            .transition()
            .attr('fill', '#fd267d');
        }
      })
      .on('mouseout', function(d) {
        if(d !== nodes[0]){
          d3.select(this)
            .transition()
            .duration(100)
            .attr('fill', '#ff7854');
        }
      })
      .on('click', (d)  => {
        console.log(d["name"])
        d3.selectAll('g > *').remove()
        this.props.findNewSimilaritiesCallback(d["name"]);
      })


    const textElements = group2
      .selectAll('text')
      .data(nodes)
      .enter().append('text')
        .text(node => node.name)
        .attr('font-size', 20)
        .attr('dx', 15)
        .attr('dy', 4)

    const link = group
      .attr("class", "links")
    .selectAll("line")
    .data(links)
    .enter().append("line")
      .attr("stroke-width", 1.5)
      .style("opacity", .6)

    simulation.on("tick", tickActions );

    const link_force =  d3.forceLink(links)
      .id(function(d) { return d.id; })

    simulation.force("links",link_force)

    function circleColor(d){
      if(d === nodes[0]) {
        return "#fd267d";
      } else {
        return "#ff7854";
      }
    }

    function circleOpacity(d){

    }

    function circleSize(d){
      if (d.strength === 1) {
        return 50
      }
      return 450 * d.strength
    }

    function tickActions() {
      node
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; });
      textElements
        .attr("x", node => node.x)
        .attr("y", node => node.y);
      link
        .attr("x1", function(d) { return d.source.x; })
        .attr("y1", function(d) { return d.source.y; })
        .attr("x2", function(d) { return d.target.x; })
        .attr("y2", function(d) { return d.target.y; });
    }
  }


  render() {
    return (
      <svg width="1100" height="900">
        <g ref="links"/>
        <g ref="nodes"/>
      </svg>
    );
  }
}


NetworkGraph.propTypes = {
  findNewSimilaritiesCallback: PropTypes.func.isRequired,
}
export default NetworkGraph;

// based on source: https://tomroth.com.au/fdg-basics/