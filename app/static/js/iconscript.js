document.addEventListener("DOMContentLoaded", function () {
    const icons = document.querySelectorAll(".icon");
    const contents = document.querySelectorAll(".scroll-list");
  
    icons.forEach((icon) => {
    icon.addEventListener("click", function () {
        console.log('IM BEING CLICKED')
        const iconId = this.id.replace("icon", "");
        contents.forEach((list) => {
        list.style.display = "none";
        });
        document.querySelector(`#list${iconId}`).style.display = "block";
        localStorage.setItem("selectedIcon", iconId);
    });
    });
    const selectedIcon = localStorage.getItem("selectedIcon");
    if (selectedIcon) {
      document.querySelector(`#list${selectedIcon}`).style.display = "block";
    }
  });

//   Active links
document.addEventListener("DOMContentLoaded", function () {
    // Get the last active link from localStorage
    const lastActiveLink = localStorage.getItem("activeLink");

    // Apply active class to the link if found
    if (lastActiveLink) {
      const link = document.querySelector(`a[href="${lastActiveLink}"]`);
      if (link) {
        link.classList.add("active");
      }
    }

    // Attach click event listener to links
    const links = document.querySelectorAll("a");
    links.forEach(link => {
      link.addEventListener("click", function (event) {
        // Remove active class from all links
        links.forEach(link => {
          link.classList.remove("active");
        });

        // Add active class to the clicked link
        this.classList.add("active");

        // Store the clicked link in localStorage
        localStorage.setItem("activeLink", this.getAttribute("href"));
      });
    });
  });