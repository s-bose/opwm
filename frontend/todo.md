- make a confirm add / error adding pop up after addition
- make the edit / delete buttons working

// modal structure for editing an existing pwd entry

- <ModalComponent :editMode="true" v-model:showModal="openEditor" site="Google" link="http://www.google.com" username="john"  password="doe" />

// modal structure for creating a new pwd entry

- <ModalComponent v-model:showModal="openCreator" />

// we need editMode flag for additional customization. i.e, icon change

- create a delete modal
