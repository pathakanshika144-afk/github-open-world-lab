const taskList = document.querySelector("#task-list");
const statusMessage = document.querySelector("#status-message");
const completedStorageKey = "open-world-checklist:completed";

function getCompletedIds() {
  try {
    return new Set(JSON.parse(localStorage.getItem(completedStorageKey) || "[]"));
  } catch (error) {
    console.warn("Saved checklist state could not be read.", error);
    return new Set();
  }
}

function saveCompletedIds(completedIds) {
  localStorage.setItem(completedStorageKey, JSON.stringify([...completedIds]));
}

function createTaskItem(task, completedIds) {
  const item = document.createElement("li");
  item.className = "task-item";
  const label = document.createElement("label");
  const checkbox = document.createElement("input");
  checkbox.type = "checkbox";
  checkbox.checked = completedIds.has(task.id) || task.completed;
  checkbox.setAttribute("aria-label", `Mark ${task.title} as complete`);
  checkbox.addEventListener("change", () => {
    if (checkbox.checked) {
      completedIds.add(task.id);
    } else {
      completedIds.delete(task.id);
    }
    saveCompletedIds(completedIds);
    item.classList.toggle("is-completed", checkbox.checked);
  });
  const title = document.createElement("strong");
  title.textContent = task.title;
  const category = document.createElement("span");
  category.className = "task-category";
  category.textContent = task.category;
  label.append(checkbox, title, category);
  item.classList.toggle("is-completed", checkbox.checked);
  item.append(label);
  return item;
}

function renderTasks(tasks) {
  taskList.innerHTML = "";
  const completedIds = getCompletedIds();

  for (const task of tasks) {
    taskList.append(createTaskItem(task, completedIds));
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
