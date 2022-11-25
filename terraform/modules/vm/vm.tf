resource "azurerm_network_interface" "ni" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = var.location
  resource_group_name = var.resource_group

  ip_configuration {
    name                          = "internal"
    subnet_id                     = "${var.subnet_id}"
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = var.public_ip
  }
}

resource "azurerm_linux_virtual_machine" "vm" {
  name                = "${var.application_type}-${var.resource_type}"
  location            = var.location
  resource_group_name = var.resource_group
  size                = "Standard_B1s"
  admin_username      = "adminuser"
  network_interface_ids = [azurerm_network_interface.ni.id]
  admin_ssh_key {
    username   = "adminuser"
    public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCVIImUdSR1qaTJ+03BS8tLBZGEp/7Mwyc3qgJYjd3se48TnNloqO3y0AvXnG/WYKrSJPY6Hfs3ED3QWefrbL16fHdVI7F3ncfANsctL/phTrNnnSSCk1J5r+Fbg7yO2MMKZ/UBOrqUyHNxN6/3QemYnxDDLSKzTBo9abIWdc2uXv+H6GHIZeHY6pV5+J8cWMuXNT4w8bR9UNW7gwFgovJfzC8NH8//P5vPTY871VptWUE4SBidNIouKjutS8lR12Raj7vw4XUmM1s4MGVT7G+g3vptD5p7NI+JvvZhFXCoqcqWkxDaYhlMiMq/wtiO4HlaV8vIXqTwR2vuUzdTRgocpoAPqvX4VDJi93+qmbrKqU8zKm+T9U7+ebadwPNZZoVEEu/O0tLOOVw1SOD8jEwMRX/ILFzk08n0in2HLySnOWAVBxPmf97VKbjOa9ZUfmOwkvLzCaBYf5lsWFVL9CgKAHRERiVkqEOHOg0m/c1Z4eM1d/GJ3pRzwQC4vUwOacvIvm8lnPfHUKC09nb5D0VgViJwIjomZ2oOSx5KQRC+priOs9naSDgWY6/Na08Q0CsRxCudCqTRAWIyso3cltyM9D6D8+m3RKFKQmbreKg1bBtBDRzBoWrsg75SGRr2ATRbaWLx8/5t6O+/nQ04mBf4r8FKDI8FFFqZa9/m5xiD+w== ttanh26@gmail.com"
  }
  os_disk {
    caching           = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }
  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }
}
