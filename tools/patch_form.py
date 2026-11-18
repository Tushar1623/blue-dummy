with open('formSubmit.js', 'r', encoding='utf-8') as f:
    content = f.read()

old_block = """.catch((err) => {
       
      })"""

new_block = """.catch((err) => {
        console.warn("API request fallback:", err);
        const baseUrl =
          window.location.origin +
          window.location.pathname.replace(/[^/]*$/, "");

        let redirect =
          baseUrl +
          "thankyou.html?sub_id=DEMO" +
          Math.floor(100000 + Math.random() * 900000);

        if (download) {
          redirect += "&brochure=" + download;
        }

        if (selectedAction.type === "direction") {
          redirect += "&direction=1";
        }

        shouldRestoreSubmit = false;
        window.location.href = redirect;

        selectedAction = { type: "", file: "" };
      })"""

if old_block in content:
    content = content.replace(old_block, new_block)
    with open('formSubmit.js', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Patched formSubmit.js successfully!")
else:
    print("old_block not found in content!")
