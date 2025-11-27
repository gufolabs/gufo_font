document.addEventListener('DOMContentLoaded', () => {
  const input = document.querySelector('#icons-search-input');
  const lists = document.querySelectorAll('.icons-list');
  const filterIcons = (needle) => {
    lists.forEach((list) => {
      list.querySelectorAll('.icon').forEach((item) => {
        const iconClass = Array.from(item.querySelector('.gf').classList)
          .find((cls) => cls !== 'gf') || '';
        const matches = needle && iconClass.toLowerCase().includes(needle);
        const show = needle.length < 3 ? true : !!matches;
        item.classList.toggle('icon--hidden', !show);
      });
    });
  };

  input.addEventListener('input', () => {
    const value = input.value.trim().toLowerCase();
    filterIcons(value);
  });

  filterIcons('');
});