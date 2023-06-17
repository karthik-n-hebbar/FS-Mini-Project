const tabs = document.querySelectorAll('.tab-btn');
const all_content = document.querySelectorAll('.content-page');

tabs.forEach((tab, index) => {
    tab.addEventListener('click', () => {
        tabs.forEach(tab => { tab.classList.remove('active') });
        tab.classList.add('active');
        all_content.forEach(content => { content.classList.remove('active') });
        all_content[index].classList.add('active');
    })
})

function submitForm() {
    document.getElementById("departure_city").form.submit();
  }