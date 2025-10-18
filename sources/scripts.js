async function all_students() {
    const generatedHTML = await window.pywebview.api.get_all_students();
    const container = document.getElementById('output-container');
    container.innerHTML = generatedHTML;
}

async function student_by_name() {
    const c = document.getElementById('student_name');
    
    if (c.value === "") {
        alert("Имя студента не может быть пустым");
    } else {
        const generatedHTML = await window.pywebview.api.get_by_name(c.value);
        const container = document.getElementById('output-container');
        container.innerHTML = generatedHTML;
    }
}

async function student_by_id() {
    const c = document.getElementById('student_id');
    
    if (c.value === "") {
        alert("ID студента не может быть пустым");
    } else {
        const generatedHTML = await window.pywebview.api.get_by_id(c.value);
        const container = document.getElementById('output-container');
        container.innerHTML = generatedHTML;
    }
}
