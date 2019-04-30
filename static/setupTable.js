/**
 * This code is imported from:
 * https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js
 */
let table = $('#table').DataTable({
    "aoColumnDefs": [
        {
            "bSortable": false,
            "aTargets": ["sorting_disabled"]
        }
    ]
});

$('.dataTables_length').addClass('bs-select');
