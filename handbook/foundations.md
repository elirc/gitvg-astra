# Foundations you can practice against Folio

Use tiny examples to understand a construct, then locate it in production-shaped code. You do not need to memorize language syntax before contributing, but you should understand the values your change moves.

## Values, objects, and collections

A value is a particular piece of data. A type describes permitted values and operations. An object groups named values. An array holds an ordered collection. In Folio, a page's id identifies it, its title is display text, and its children form a tree. Two pages can have the same title and still be different pages.

```typescript
type PracticePage = { id: string; title: string; favorite: boolean };
const pages: PracticePage[] = [
  { id: 'a', title: 'Getting started', favorite: true },
  { id: 'b', title: 'Runbooks', favorite: false },
];
const titles = pages.filter(page => page.favorite).map(page => page.title);
```

Predict `titles` before running it. `filter` selects elements; `map` transforms them. Neither call above changes the source array. Changing `page.favorite` inside the callback would still mutate the object; a new array does not automatically deep-copy its elements. Find `flatMap` in [FavoritesList](../../folio-app/client/src/components/FavoritesList.tsx) and explain why recursion is needed for nested pages.

**Practice:** Write `countFavorites`, then return favorite titles without changing the input. Cover empty input and duplicate titles. Use ids for identity. Next implement the same transformation in C# using `Where`, `Select`, and `Count`, comparing it to a loop. Keep scratch work under your `astra/work` directory.

## Null, undefined, and defaults

In the server, `Guid? ParentId` allows a page to have no parent. In TypeScript, a field might be `string | null`, optional, or absent because data has not loaded yet. These are different states. An empty title `""` is present but may fail a business rule. A root page's null parent is valid domain data.

`x ?? fallback` chooses a fallback for null/undefined; `x || fallback` also replaces values such as `0`, `false`, and `""`. Predict the result for all five inputs. Then find `icon ??` in the client and explain its purpose. Do not silence uncertainty with `!` or a cast before establishing why a value must exist.

## Functions and side effects

A pure function returns the same output for the same input and does not change outside state. Filtering favorite titles can be pure. Calling the API, writing to SQLite, logging, and reading the current clock are side effects. Pure functions are easy to test with a table; side effects need a controlled boundary.

Follow `renamePage` in [folio.ts](../../folio-app/client/src/api/folio.ts). It returns a promise for a server response, not a locally renamed page. On the server, `UpdateAsync` coordinates several side effects; extracting every line into a method would not automatically improve its design.

## Async/await and failure

`await` suspends an asynchronous operation's continuation until its result is available. It does not mean the whole application stops. A rejected promise or thrown asynchronous exception reaches a matching error handler. Two requests can finish in a different order from their start order.

Draw this timeline: query A starts, query B starts, B finishes, A finishes. Which response should the search box display? [useAsync](../../folio-app/client/src/hooks/useAsync.ts) combines an abort signal with an `active` guard. Cancellation is a request to stop; the state guard protects against a response completing after the effect is obsolete.

**Practice:** Make two manually controlled promises in a client test and resolve them in reverse order. Explain why waiting a fixed number of milliseconds is weaker evidence than controlling completion.

## Reading C# without guessing

Read [PageDtos.cs](../../folio-app/server/Folio.Api/Contracts/PageDtos.cs). `record` defines a data-oriented type. Constructor parameters describe the request fields. `[Required]` and `[MaxLength(400)]` are validation metadata, not comments. `Task<T>` represents an asynchronous result of type T. `CancellationToken` carries a cancellation request through asynchronous operations.

Read the controller's switch expression: one service status maps to one HTTP response. Then inspect `ServiceResult<T>` to see how a successful value differs from an error. Do not conflate null, invalid input, forbidden access, and absent resources; the caller needs different behavior for each.

## HTTP, JSON, and the database

HTTP is the request/response boundary between browser and server. JSON represents values crossing it. TypeScript types disappear at runtime, so a typed fetch wrapper can still receive an unexpected response. Server validation and tests remain necessary.

A database persists state beyond a process lifetime. The browser may show an unsaved input while the stored title remains unchanged. EF tracks an entity change until `SaveChangesAsync` persists it. A successful render therefore proves neither persistence nor permission. Reload the resource through the server when testing those guarantees.

## Completion check

Without notes, explain identity versus title, derived data versus state, null versus empty, a promise versus its resolved value, and a DTO versus an entity. Give a Folio filename for each. If you cannot yet do that, repeat one tiny exercise and ask for review before increasing the task size.
