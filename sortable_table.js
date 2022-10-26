// Alphatically sort entries in a table


function make_sortable(table_node) {
  var head_nodes = table_node.querySelectorAll("thead th");

  head_nodes.forEach((head_node, column_index) => {
    head_node.addEventListener('click', () => {
      console.log("Sorting", column_index)
      let asc = true

      if (head_node.classList.contains("sort-asc")) {
        asc = false
      }

      head_nodes.forEach((h) => {
        h.classList.remove("sort-asc");
        h.classList.remove("sort-desc");
      })

      if (asc) {
        head_node.classList.toggle("sort-asc")
      } else {
        head_node.classList.toggle("sort-desc")
      }

      sort_table(table_node, column_index, asc)
    });

  });
}



function sort_table(table_node, column_index, asc) {
  console.log("Sorting table by", column_index, asc)

  let table_body = table_node.querySelector('tbody');
  let row_nodes = [];
  let table_data = [];

  let rows = table_body.children

  for (var row_index = 0; row_index < rows.length; row_index++) {
    row = table_body.children[row_index]
    row_nodes.push(row);

    let data_cell = row.querySelectorAll('th, td')[column_index];


    table_data.push({
      index: row_index,
      value: data_cell.innerText,
    })

    console.log("Pushing row", row_index, data_cell.innerText)
  }

  console.log(table_data)

  table_data.sort((a, b) => {
    if (a.value === b.value) return 0;
    return (asc != (a.value > b.value)) ? -1 : 1;
  });

  // remove all rows
  while (table_body.firstChild) {
    console.log("deleting row")
    table_body.removeChild(table_body.lastChild);
  }

  // add in all row
  table_data.forEach((data_cell) => {
    console.log("adding row")
    table_body.appendChild(row_nodes[data_cell.index]);
  })
}



window.addEventListener('load', function () {
  var sortables = document.querySelectorAll('div.sortable table');
  sortables.forEach(make_sortable)
});
