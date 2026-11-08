const input =  document.querySelector('#searchinput');
const rows = document.querySelectorAll('#tableBody tr');

input.addEventListener('input', (event)=>{
    const query = event.target.value.toLowerCase().trim();
    rows.forEach(row => {
        const rowText = row.textContent.toLowerCase();
        const match = rowText.includes(query);
        row.style.display = match ? '':'none';
    });
});