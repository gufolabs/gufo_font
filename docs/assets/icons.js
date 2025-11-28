document.addEventListener('DOMContentLoaded', () => {
  const input = document.querySelector('#gufo-search-input');
  const lists = document.querySelectorAll('.icons-list');
  const status = document.querySelector('#gufo-search-status');
  const filterIcons = (needle) => {
    lists.forEach((list) => {
      list.querySelectorAll('.icon').forEach((item) => {
        const iconClass = Array.from(item.querySelector('.gf').classList)
          .find((cls) => cls !== 'gf') || '';
        const matches = needle && iconClass.toLowerCase().includes(needle);
        const show = needle.length < 1 ? true : !!matches;
        item.classList.toggle('icon--hidden', !show);
      });
    });
  };

  input.addEventListener('input', () => {
    const value = input.value.trim().toLowerCase();
    filterIcons(value);
  });

  let prevStatus = status.value;
  status.addEventListener('change', (event) => {
    const nextStatus = event.target.value;
    document.querySelectorAll('i.gf').forEach((icon) => {
      if(prevStatus) {
        icon.classList.remove(`${prevStatus}`);
      }
      icon.classList.add(`${nextStatus}`);
    });
    prevStatus = nextStatus;
  });
  filterIcons('');
});
