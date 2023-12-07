import React, { useState, useEffect, useRef } from 'react';
import * as d3 from 'd3';

function TreeVisualization() {
  const [tree, setTree] = useState(null);
  const [shortestPath, setShortestPath] = useState([]);
  const [graphData, setGraphData] = useState('1 1 0 0 1 0 0 0 0 1\n0 1 1 1 1 1 0 1 1 0\n0 1 1 1 1 1 0 1 1 0\n0 1 1 1 1 1 0 1 1 0\n0 0 0 0 0 1 1 1 1 1');
  const [graphRows, setGraphRows] = useState([]);
  const [currentLevel, setCurrentLevel] = useState(0);
  const [ballPositions, setBallPositions] = useState([{ x: 0, y: 0, color: 'orange' }]); // 복수의 공 위치를 위한 배열
  const svgRef = useRef();
  const dx = [1, 0, -1, 0];
  const dy = [0, -1, 0, 1];
  let level = [];
  const [path, setPath] = useState([]);

  const handleGraphInputChange = (event) => {
    setGraphData(event.target.value);
  };

  const handleSubmit = () => {
    const newGraphRows = graphData.split('\n').map(row => row.split(' ').map(Number));
    setGraphRows(newGraphRows);
    setCurrentLevel(0);
    setHighlightShortestPath(false);
    setBallPositions([{ x: 0, y: 0, color: 'orange' }]);
  };

  const [highlightShortestPath, setHighlightShortestPath] = useState(false);
  const handleHighlightToggle = () => {
    setHighlightShortestPath(!highlightShortestPath);
  };//최단 경로를 강조

 //레벨 증가 함수 
	const handleIncreaseLevel = () => {
		setCurrentLevel(prevLevel => {
			const newLevel = prevLevel + 1;
	
			// 목적지 노드의 레벨을 확인
			const end = { x: graphRows.length - 1, y: graphRows[0].length - 1 };
			const endKey = end.x + ',' + end.y;
			const destinationNode = findNode(tree, endKey);
			// 최단 경로로 도착했을 시
			if (destinationNode && newLevel >= destinationNode.level) {
				// 최단 경로의 공들만 표시
				const updatedBallPositions = path.map(coord => {
					const [x, y] = coord.split(',').map(Number);
					return { x, y, color: 'skyblue' };
				});
				setBallPositions(updatedBallPositions);
				setHighlightShortestPath(true); //최단경로 시에 강조
			} else {
				// 현재 레벨에 해당하는 공들만 표시
				const currentLevelPositions = level[newLevel]?.map(coord => {
					const [x, y] = coord.split(',').map(Number);
					return { x, y, color: 'orange' };
				}) || [];
	
				setBallPositions(currentLevelPositions);
				setHighlightShortestPath(false);
			}
	
			return newLevel;
		});
	};
	
	
	
  const bfsTree = (start, end, graph) => {
    const rootNode = { value: start.toString(), children: [], level: 0 };
    const visited = {}; //방문한 노드 저장
    const queue = []; //탐색을 위한 큐
    queue.push([null, start]);
    visited[start.toString()] = rootNode;
	//BFS 탐색
    while (queue.length > 0) {
      const now = queue.shift(); 
      const [x, y] = now[1];
      const key = x + ',' + y;

      for (let i = 0; i < 4; i++) {
        const nx = x + dx[i]; //다음 x좌표
        const ny = y + dy[i]; //다음 y좌표
        const childKey = nx + ',' + ny; //다음 위치의 키값

        if (nx < 0 || ny < 0 || nx >= graph.length || ny >= graph[0].length) {
          continue;
        }
        if (visited[childKey] || graph[nx][ny] === 0) {
          continue;
        }

        graph[nx][ny] = graph[x][y] + 1;
        queue.push([[x, y], [nx, ny]]); //큐에 다음 위치 추가
        const newNode = { value: childKey, children: [], level: visited[key].level + 1 };
        visited[key].children.push(newNode); // 현재 노드의 자식으로 추가
        visited[childKey] = newNode; //방문한 노드로 표시
      }
    }

    return rootNode; //트리의 루트노드 반환
  };

  const findPathToDestination = (node, destination) => {
    if (!node || node.value === destination) return [destination]; //노드가 없거나 목적지와 일치하는 경우 경로 반환

	// 현재 노드의 자식들을 순회하며 목적지를 찾음
    for (const child of node.children) {
      const path = findPathToDestination(child, destination);
      if (path.length) return [node.value, ...path];
    }

    return [];
  };

  const groupNodesByLevel = (root) => {
    const nodesByLevel = {};

	//트리를 순회하며 각 노드를 레벨별로 그룹화
    const traverseTree = (node) => {
      if (!node) return;

      const level = node.level;
	  //해당 레벨의 노드 배열이 존재하지 않으면 새로 노드를 생성
      if (!nodesByLevel[level]) {
        nodesByLevel[level] = [];
      }
      nodesByLevel[level].push(node.value.toString());
	  //각 자식 노드에 대해 재귀적으로 함수 호출하여 트리를 순회
      node.children.forEach((child) => {
        traverseTree(child);
      });
    };
	//레벨별로 노드를 그룹화
    traverseTree(root);
    return nodesByLevel;
  };
  
	// 주어진 트리에서 목적지 노드와 목적지 레벨을 기준으로 노드를 제거하는 함수
const removeNodesAboveAndOnDestinationLevel = (root, destination, destinationLevel) => {
	if (!root) return null;
  
	// 목적지와 같은 레벨이지만 목적지 노드가 아닌 경우 제거
	if (root.level === destinationLevel && root.value !== destination) {
	  return null;
	}
  
	// 목적지 레벨보다 높은 노드 제거
	if (root.level > destinationLevel) {
	  return null;
	}
  
	// 자식 노드들을 재귀적으로 처리하여 필요한 노드만 필터링
	root.children = root.children
	  .map(child => removeNodesAboveAndOnDestinationLevel(child, destination, destinationLevel))
	  .filter(child => child !== null);
  
	return root;
  };
  
  // 트리에서 주어진 값을 가진 노드를 찾는 함수
  const findNode = (node, value) => {
	if (!node) return null;
	if (node.value === value) return node;
  
	// 자식 노드들을 반복하며 주어진 값을 가진 노드를 찾음
	for (let child of node.children) {
	  const found = findNode(child, value);
	  if (found) return found;
	}
  
	return null;
  };
  
  useEffect(() => {
	if (graphRows.length > 0) {
	  const end = { x: graphRows.length - 1, y: graphRows[0].length - 1 };
	  const rootNode = bfsTree([0, 0], end, graphRows);
  
	  // 목적지 노드의 레벨 찾기
	  const destinationNode = findNode(rootNode, end.x + ',' + end.y);
	  const destinationLevel = destinationNode ? destinationNode.level : -1;
  
	  // 목적지 레벨 이상 및 같은 노드 제거
	  const filteredRoot = removeNodesAboveAndOnDestinationLevel(rootNode, end.x + ',' + end.y, destinationLevel);
  
	  const newPath = findPathToDestination(filteredRoot, end.x + ',' + end.y);
	  setPath(newPath);
	  setShortestPath(newPath);
	  setTree(filteredRoot);
	}
  }, [graphRows]);
  
  useEffect(() => {
	if (tree) {
	  const nodesByLevel = groupNodesByLevel(tree);
	  level = { ...nodesByLevel };
  
	  const margin = { top: 10, right: 120, bottom: 10, left: 40 };
	  const width = 960 - margin.right - margin.left;
	  const height = 500 - margin.top - margin.bottom;
  
	  // SVG 요소 초기화
	  d3.select(svgRef.current).selectAll("*").remove();
	  const svg = d3.select(svgRef.current)
		.attr("width", width + margin.right + margin.left)
		.attr("height", height + margin.top + margin.bottom)
		.append("g")
		.attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  
	  // 트리 레이아웃 설정
	  const root = d3.hierarchy(tree);
	  const treeLayout = d3.tree().size([height, width]);
	  treeLayout(root);
  
	  // 레벨 필터링
	  const filteredNodes = root.descendants().filter(node => node.depth <= currentLevel);
	  const filteredLinks = root.links().filter(link => {
		return filteredNodes.includes(link.source) && filteredNodes.includes(link.target);
	  });
  
	  // 노드와 링크 그리기
	  svg.selectAll(".link")
		.data(filteredLinks)
		.enter().append("path")
		.attr("class", "link")
		.style("stroke", d => {
		  if (highlightShortestPath && shortestPath.includes(d.target.data.name)) {
			return "red";
		  }
		  return "#555";
		})
		.style("stroke-width", 1.5)
		.attr("d", d3.linkHorizontal()
		  .x(d => d.y)
		  .y(d => d.x));
  
	  const nodes = svg.selectAll(".node")
		.data(filteredNodes)
		.enter().append("g")
		.attr("class", "node")
		.attr("transform", d => "translate(" + d.y + "," + d.x + ")");
  
	  // 직사각형으로 노드 표현
	  nodes.append("rect")
		.attr("width", 40)  
		.attr("height", 20)  
		.attr("x", -20)  
		.attr("y", -10) 
		.style("fill", d => shortestPath.includes(d.data.value) && highlightShortestPath ? "skyblue" : "orange");
  
	  // 노드 위에 텍스트 추가
	  nodes.append("text")
		.attr("dy", ".35em")
		.attr("text-anchor", "middle")
		.text(d => {
		  const parts = d.data.value.split(',').map(part => parseInt(part, 10) + 1); // 숫자로 변환 후 1 더하기
		  return `${parts[1]},${parts[0]}`; // 순서 바꾸어서 결합
		})
		.style("fill", "black")
		.style("font-size", "15px")
		.style("font-family", "monospace");
  
	  if (highlightShortestPath) {
		// 노드 강조
		svg.selectAll(".node")
		  .style("fill", d => shortestPath.includes(d.data.value) ? "red" : "#999");
  
		// 링크 강조
		svg.selectAll(".link")
		  .style("stroke", d => {
			const sourceIndex = shortestPath.indexOf(d.source.data.value);
			const targetIndex = shortestPath.indexOf(d.target.data.value);
			return (sourceIndex !== -1 && targetIndex === sourceIndex + 1) ? "skyblue" : "#555";
		  })
		  .style("stroke-width", d => {
			const sourceIndex = shortestPath.indexOf(d.source.data.value);
			const targetIndex = shortestPath.indexOf(d.target.data.value);
			return (sourceIndex !== -1 && targetIndex === sourceIndex + 1) ? 1 : 2.0;
		  });
	  }
	}
  }, [tree, shortestPath, highlightShortestPath, currentLevel]);
  
	
	  return (
		<div>
			
			<div>
		  <textarea
			placeholder="Enter graph data…"
			value={graphData}
			onChange={handleGraphInputChange}
			rows={5}
			cols={30}
		  />
			</div>
			<div>
				<button onClick={handleSubmit}>Build a maze</button>
			</div>
			<br/>
			{/* 미로 시각화 */}
			<div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-start' }}>
				{graphRows.map((row, rowIndex) => (
					<div key={rowIndex} style={{ display: 'flex' }}>
						{row.map((cell, colIndex) => (
							<div
								key={colIndex}
								style={{
									width: '30px',
									height: '30px',
									backgroundColor: cell === 0 ? 'black' : 'white',
									border: '1px solid black',
									position: 'relative',
								}}
							>
								{/* 현재 위치 시각화 */}
								{ballPositions.some(pos => pos.x === rowIndex && pos.y === colIndex) && (
									<div
										style={{
											width: '30px',
											height: '30px',
											backgroundColor: ballPositions.find(pos => pos.x === rowIndex && pos.y === colIndex).color,
											borderRadius: '50%',
											position: 'absolute',
											top: '50%',
											left: '50%',
											transform: 'translate(-50%, -50%)',
										}}
									></div>
								)}
							</div>
						))}
					</div>
				))}
			</div>
			<br/>
			<div>
				<button onClick={handleIncreaseLevel}>Go 1 step</button>
			</div>
			

			<div>
		  <svg ref={svgRef}></svg>
					{highlightShortestPath && shortestPath.length > 0 && (
     		<div style={{ fontSize: '18px', fontWeight: 'bold' }}>
        	최단 경로 길이: {shortestPath.length}
      	</div>
    )}
			</div>
		</div>
	  );
	}
	
export default TreeVisualization;
