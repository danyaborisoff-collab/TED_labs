import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


def on_activate(app):
    win = Gtk.ApplicationWindow(application=app, title="Тест доступности")
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8,
                  margin_top=12, margin_bottom=12, margin_start=12, margin_end=12)
    entry = Gtk.Entry()                                       # барьер: поле без подписи
    search = Gtk.Button(icon_name="system-search-symbolic")  # барьер: кнопка-иконка без имени
    remember = Gtk.CheckButton(label="Запомнить")

    # Диалог с результатом — нужен для регистрации window:create / window:activate
    def on_search(_button):
        dialog = Gtk.AlertDialog(message="Результаты поиска",
                                 detail=f"По запросу «{entry.get_text()}» ничего не найдено",
                                 buttons=["Закрыть"])
        dialog.choose(win, None, None)

    search.connect("clicked", on_search)
    for widget in (entry, search, remember):
        box.append(widget)
    win.set_child(box)
    win.present()


app = Gtk.Application(application_id="ru.itmo.a11ylab")
app.connect("activate", on_activate)
app.run()
