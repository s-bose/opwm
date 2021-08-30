<template>
  <div class="w-full md:w-3/5 mx-auto p-8">
    <p>Open <strong>one</strong></p>
    <div class="shadow-md">
      <div class="tab w-full overflow-hidden border-t">
        <input class="absolute opacity-0" id="tab-single-one" type="radio" name="tabs2" />
        <label class="block p-5 leading-normal cursor-pointer" for="tab-single-one">Label One</label>
        <div class="tab-content overflow-hidden border-l-2 bg-gray-100 border-indigo-500 leading-normal">
          <p class="p-5">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tenetur, architecto, explicabo perferendis nostrum, maxime impedit atque odit sunt
            pariatur illo obcaecati soluta molestias iure facere dolorum adipisci eum? Saepe, itaque.
          </p>
        </div>
      </div>
      <div class="tab w-full overflow-hidden border-t">
        <input class="absolute opacity-0" id="tab-single-two" type="radio" name="tabs2" />
        <label class="block p-5 leading-normal cursor-pointer" for="tab-single-two">Label Two</label>
        <div class="tab-content overflow-hidden border-l-2 bg-gray-100 border-indigo-500 leading-normal">
          <p class="p-5">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tenetur, architecto, explicabo perferendis nostrum, maxime impedit atque odit sunt
            pariatur illo obcaecati soluta molestias iure facere dolorum adipisci eum? Saepe, itaque.
          </p>
        </div>
      </div>
      <div class="tab w-full overflow-hidden border-t">
        <input class="absolute opacity-0" id="tab-single-three" type="radio" name="tabs2" />
        <label class="block p-5 leading-normal cursor-pointer" for="tab-single-three">Label Three</label>
        <div class="tab-content overflow-hidden border-l-2 bg-gray-100 border-indigo-500 leading-normal">
          <p class="p-5">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Tenetur, architecto, explicabo perferendis nostrum, maxime impedit atque odit sunt
            pariatur illo obcaecati soluta molestias iure facere dolorum adipisci eum? Saepe, itaque.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PasswordListItem",
  components: {},
};
</script>

<style>
</style>