document.addEventListener('DOMContentLoaded', () => {
  const input = document.querySelector('[data-component="search-input"]');
  const lists = document.querySelectorAll('[data-component="icons-list"]');
  const styleSelect = document.querySelector('[data-component="style-select"]');
  
  if (!input || !styleSelect) return;

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

  let prevStyle = styleSelect.value;
  
  styleSelect.addEventListener('change', (event) => {
    const nextStyle = event.target.value;
    const icons = document.querySelectorAll('[data-type="icon-element"]');
    
    icons.forEach((icon) => {
      if (prevStyle) icon.classList.remove(prevStyle);
      if (nextStyle) icon.classList.add(nextStyle);
    });
    
    prevStyle = nextStyle;
  });

  filterIcons('')
});
