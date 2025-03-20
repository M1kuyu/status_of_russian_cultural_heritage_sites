<?php include 'header.php'; ?>
<h2>Журнал изменений</h2>

<!-- Фильтры и настройки пагинации можно добавить по желанию -->
<div id="changesContainer">
    <!-- Здесь будут динамически подгружаться записи журнала -->
</div>

<div class="pagination">
    <button onclick="prevPage()">Предыдущая</button>
    <span id="pageInfo">Страница 1</span>
    <button onclick="nextPage()">Следующая</button>
    <!-- Выбор количества элементов на странице -->
    <select id="itemsPerPage" onchange="fetchChanges(1)">
        <option value="25">25</option>
        <option value="50">50</option>
        <option value="100">100</option>
    </select>
</div>

<script>
let currentPage = 1;

function fetchChanges(page) {
    currentPage = page;
    const itemsPerPage = document.getElementById('itemsPerPage').value;
    
    // Запрос к бэкенду; предполагается, что эндпоинт поддерживает параметры пагинации
    fetch(`http://127.0.0.1:8000/changes/?page=${page}&limit=${itemsPerPage}`)
        .then(response => response.json())
        .then(data => {
            let html = '';
            if (data.length > 0) {
                data.forEach(change => {
                    html += `<div class="change-card">
                                <h3>Объект: ${change.global_id}</h3>
                                <p><strong>Тип изменения:</strong> ${change.status}</p>
                                <p><strong>Поле:</strong> ${change.field_name ? change.field_name : '-'}</p>
                                <p><strong>Старая величина:</strong> ${change.old_value ? change.old_value : '-'}</p>
                                <p><strong>Новая величина:</strong> ${change.new_value ? change.new_value : '-'}</p>
                                <p><strong>Дата изменения:</strong> ${change.change_date}</p>
                                <p><strong>Версия датасета:</strong> ${change.dataset_version}</p>
                                <p><strong>Название объекта:</strong> ${change.ObjectNameOnDoc ? change.ObjectNameOnDoc : '-'}</p>
                                <p><strong>Адрес:</strong> ${change.Addresses ? change.Addresses : '-'}</p>
                             </div>`;
                });
            } else {
                html = '<p>Записей не найдено.</p>';
            }
            document.getElementById('changesContainer').innerHTML = html;
            document.getElementById('pageInfo').innerText = `Страница ${currentPage}`;
        })
        .catch(error => console.error('Ошибка при получении данных:', error));
}

function nextPage() {
    currentPage++;
    fetchChanges(currentPage);
}

function prevPage() {
    if (currentPage > 1) {
        currentPage--;
        fetchChanges(currentPage);
    }
}

// Начальная загрузка
fetchChanges(1);
</script>

<?php include 'footer.php'; ?>
