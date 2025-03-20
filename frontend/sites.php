<?php include 'header.php'; ?>

<h2>Объекты культурного наследия</h2>

<div class="filters">
    <!-- Поле для живого поиска -->
    <input type="text" id="searchInput" placeholder="Поиск объектов...">
    <!-- Выбор количества элементов на странице -->
    <select id="itemsPerPage">
        <option value="25">25</option>
        <option value="50">50</option>
        <option value="100">100</option>
    </select>
</div>

<div id="sitesContainer">
    <!-- Здесь будут отображаться объекты -->
</div>

<div class="pagination">
    <button onclick="prevPage()">Предыдущая</button>
    <span id="pageInfo">Страница 1</span>
    <button onclick="nextPage()">Следующая</button>
</div>

<script>
    let allSites = [];          // Все данные с API
    let filteredSites = [];     // Отфильтрованные данные
    let currentPage = 1;        // Текущая страница
    let itemsPerPage = 25;      // Количество элементов на странице

    // Функция для загрузки всех данных с API
    function loadAllSites() {
        fetch("http://127.0.0.1:8000/sites/")
            .then(response => response.json())
            .then(data => {
                allSites = data;
                filteredSites = data;
                displaySites();
            })
            .catch(error => console.error('Ошибка при получении данных:', error));
    }

    // Функция для отображения текущей страницы данных
    function displaySites() {
        const start = (currentPage - 1) * itemsPerPage;
        const end = start + itemsPerPage;
        const pageSites = filteredSites.slice(start, end);

        let html = '';
        if (pageSites.length > 0) {
            pageSites.forEach(site => {
                html += `<div class="site-card">
                            <h3>${site.ObjectNameOnDoc || 'Без названия'}</h3>
                            <p><strong>Категория:</strong> ${site.Category || 'N/A'}</p>
                            <p><strong>Расположение:</strong> ${site.Location || 'N/A'}</p>
                            <p><strong>Статус:</strong> ${site.SecurityStatus || 'N/A'}</p>
                        </div>`;
            });
        } else {
            html = '<p>Объекты не найдены.</p>';
        }
        document.getElementById('sitesContainer').innerHTML = html;
        document.getElementById('pageInfo').innerText = `Страница ${currentPage}`;
    }

    // Функция для фильтрации данных по поисковому запросу
    function filterSites() {
        const searchTerm = document.getElementById('searchInput').value.toLowerCase();
        filteredSites = allSites.filter(site => {
            return (
                site.ObjectNameOnDoc?.toLowerCase().includes(searchTerm) ||
                site.Category?.toLowerCase().includes(searchTerm) ||
                site.Location?.toLowerCase().includes(searchTerm) ||
                site.SecurityStatus?.toLowerCase().includes(searchTerm)
            );
        });
        currentPage = 1; // Сброс на первую страницу при новом поиске
        displaySites();
    }

    // Функция debounce для задержки выполнения фильтрации
    function debounce(func, delay) {
        let timeoutId;
        return function(...args) {
            clearTimeout(timeoutId);
            timeoutId = setTimeout(() => func.apply(this, args), delay);
        };
    }

    const debouncedFilterSites = debounce(filterSites, 300);

    // Обработчик события для поля поиска
    document.getElementById('searchInput').addEventListener('input', debouncedFilterSites);

    // Обработчик события для изменения количества элементов на странице
    document.getElementById('itemsPerPage').addEventListener('change', () => {
        itemsPerPage = parseInt(document.getElementById('itemsPerPage').value);
        currentPage = 1; // Сброс на первую страницу
        displaySites();
    });

    // Функция для перехода на следующую страницу
    function nextPage() {
        const maxPage = Math.ceil(filteredSites.length / itemsPerPage);
        if (currentPage < maxPage) {
            currentPage++;
            displaySites();
        }
    }

    // Функция для перехода на предыдущую страницу
    function prevPage() {
        if (currentPage > 1) {
            currentPage--;
            displaySites();
        }
    }

    // Загрузка данных при открытии страницы
    loadAllSites();
</script>

<?php include 'footer.php'; ?>