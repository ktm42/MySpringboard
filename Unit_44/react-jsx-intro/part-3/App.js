function App() {
    return (
      <div>
        <Person
          name="Amy"
          age={42}
          hobbies={["bowling", "watching tv", "drinking beer"]}
        />
        <Person name="Wesley" age={32} hobbies={["painting", "gambling"]} />
        <Person
          name="Toby"
          age={15}
          hobbies={["skateboarding", "making prank calls"]}
        />
        <Person
          name="Ryan"
          age={8}
          hobbies={["reading", "saxophone", "eating vegetables"]}
        />
      </div>
    );
  }