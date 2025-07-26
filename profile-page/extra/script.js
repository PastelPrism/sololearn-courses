(() => {
  
  const dayEls     = document.querySelectorAll('#streak ul li');
  const currentEl  = document.getElementById('current-count');
  const longestEl  = document.getElementById('longest-count');


  let streakData = JSON.parse(localStorage.getItem('streakData')) || {
    days:    [false, false, false, false, false, false, false],
    longest: 0
  };

 
  function render() {
    dayEls.forEach((el, idx) => {
      el.classList.toggle('active-day', streakData.days[idx]);
      el.classList.toggle('inactive-day', !streakData.days[idx]);
    });

    const current = calcCurrent();
    currentEl.textContent = current;
    longestEl.textContent = streakData.longest;
  }


  function calcCurrent() {
    let count        = 0;
    const prevLongest = streakData.longest;

    for (let i = streakData.days.length - 1; i >= 0; i--) {
      if (!streakData.days[i]) break;
      count++;
    }

    if (count > prevLongest) {
      streakData.longest = count;
      persist();
      celebrate();
    }

    return count;
  }

  
  function persist() {
    localStorage.setItem('streakData', JSON.stringify(streakData));
  }

 
  function celebrate() {
    
    confetti({
      particleCount: 120,
      spread:        70,
      origin:        { x: 0.5, y: 0.2 }
    });

    
    setTimeout(() => {
      confetti({
        particleCount: 90,
        spread:        100,
        origin:        { x: 0.5, y: 0.1 }
      });
    }, 300);
  }

  dayEls.forEach((el, idx) => {
    el.addEventListener('click', () => {
      streakData.days[idx] = !streakData.days[idx];
      persist();
      render();
    });
  });

  render();
})();
