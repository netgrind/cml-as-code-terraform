resource "iosxe_interface_loopback" "management_loopback" {
    for_each = { for router in var.routers : router.name => router }

  description                = "Management Loopback" 
  ipv4_address               = "1.1.1.1" 
  ipv4_address_mask          = "255.255.255.255" 
  name                       = 1
}