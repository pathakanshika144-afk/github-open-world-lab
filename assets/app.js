const taskList = document.querySelector("#task-list");
const statusMessage = document.querySelector("#status-message");

function renderTasks(tasks) {
  taskList.innerHTML = "";

  for (const task of tasks) {
    const item = document.createElement("li");
    item.className = "task-item";
    item.innerHTML = `
      <strong>${task.title}</strong>
      <span class="task-category">${task.category}</span>
    `;
    taskList.append(item);
  }

  statusMessage.textContent = `${tasks.length} tasks ready to explore.`;
}

async function loadTasks() {
  try {
    const response = await fetch("data/tasks.json");
    if (!response.ok) {
      throw new Error(`Could not load tasks: ${response.status}`);
    }
    renderTasks(await response.json());
  } catch (error) {
    statusMessage.textContent = "The checklist could not be loaded. Please try again later.";
    console.error(error);
  }
}

loadTasks();
