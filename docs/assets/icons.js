document.addEventListener('DOMContentLoaded', () => {
  const input = document.querySelector('[data-component="search-input"]');
  const lists = document.querySelectorAll('[data-component="icons-list"]');
  const styleSelect = document.querySelector('[data-component="style-select"]');
  const dialog = document.getElementById('gufo-icon-dialog');
  const hash = window.location.hash.slice(1);
  let prevStyle = styleSelect.value;

  if (!input || !styleSelect) return;

  if (hash) {
    showIconDialog();
  }

  const filterIcons = (needle) => {
    lists.forEach((list) => {
      list.querySelectorAll('[data-type="icon"]').forEach((item) => {
        const iconName = item.dataset.iconName || '';
        const matches = iconName.toLowerCase().includes(needle);
        item.classList.toggle('icon--hidden', needle.length > 0 && !matches);
      });
    });
  };

  input.addEventListener('input', () => {
    filterIcons(input.value.trim().toLowerCase());
  });

  
  styleSelect.addEventListener('change', (event) => {
    const nextStyle = event.target.value;
    const icons = document.querySelectorAll('[data-type="icon-element"]');
    
    icons.forEach((icon) => {
      if (prevStyle) icon.classList.remove(prevStyle);
      if (nextStyle) icon.classList.add(nextStyle);
    });
    
    prevStyle = nextStyle;
  });

  dialog.addEventListener('click', (e) => {
      const rect = dialog.getBoundingClientRect();
      if (
        e.clientX < rect.left ||
        e.clientX > rect.right ||
        e.clientY < rect.top ||
        e.clientY > rect.bottom
      ) {
        closeDialog();
      }
  });
  
  filterIcons('');
});

function showIconDialog(el) {
  const dialog = document.getElementById('gufo-icon-dialog');
  const titleEl = dialog.querySelector('.dialog-header .dialog-title-text');
  const codeEl = dialog.querySelector('.dialog-content-code');
  const iconEl = dialog.querySelector('.dialog-content-icon i');
  const descriptionEl = dialog.querySelector('.dialog-content-description');
  const versionEl = dialog.querySelector('.dialog-content-version');
  let name, code;
  if (el) {
    const url = new URL(window.location.href);
    name = el.dataset.iconName;
    code = parseInt(el.dataset.iconCode).toString(16).toUpperCase();
    url.hash = name;
    window.location.href = url.toString();
  } else {
    const hash = window.location.hash.slice(1);
    const iconEl = document.querySelector(`[data-icon-name="${hash}"]`);
    if (!iconEl) return;
    name = iconEl.dataset.iconName;
    code = parseInt(iconEl.dataset.iconCode).toString(16).toUpperCase();
    el = iconEl;
  }
  iconEl.className = `gf ${name}`;
  titleEl.textContent = `Icon: ${name}`;
  codeEl.textContent = code;
  descriptionEl.textContent = el.dataset.iconDescription || '-';
  versionEl.textContent = el.dataset.iconVersion || '-';
  titleEl.nextElementSibling.dataset.value = name; // for copy IconName to clipboard
  codeEl.nextElementSibling.dataset.value = code; // for copy IconCode to clipboard
  dialog.showModal()
};

function closeDialog() {
  const dialog = document.getElementById('gufo-icon-dialog');
  const url = new URL(window.location.href);
  url.hash = '';
  window.history.replaceState(null, '', url.toString());
  dialog.close();
};

function copyToClipboard(el) {

  navigator.clipboard.writeText(el.dataset.value || '')
    .then(() => animateCopyIcon(el))
    .catch(console.error);
}

function animateCopyIcon(el) {
  const copiedIcon = ['copy-s'];
  const originalIcon = 'copy-o';

  el.classList.remove(...copiedIcon);
  el.classList.add(originalIcon);

  el.classList.remove(originalIcon);
  el.classList.add(...copiedIcon);
  setTimeout(() => {
    el.classList.remove(...copiedIcon);
    el.classList.add(originalIcon);
  }, 2000);
}