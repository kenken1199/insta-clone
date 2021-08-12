import React from "react";
import ReactDOM from "react-dom";

ReactDOM.render(
  <React.StrictMode>
    <Layout />
  </React.StrictMode>,
  document.getElementById('root')
);

ReactDOM.render(
  <React.StrictMode>
    <Layout2 />
  </React.StrictMode>,
  document.getElementById('root2')
);

ReactDOM.render(
  <React.StrictMode>
    <PersonList />
  </React.StrictMode>,
  document.getElementById('root3')
);